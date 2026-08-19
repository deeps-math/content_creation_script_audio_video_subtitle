import requests
import json
import time
import os
import shutil
import random

COMFY_URL = "http://127.0.0.1:8188"

COMFY_OUTPUT_FOLDER = "C:/Users/deepa/imageai/ComfyUI/output"

FINAL_IMAGE_PATH = "output/image.png"


def generate_single_image(prompt, negative_prompt):

    print("🎨 Generating image...")

    # -----------------------------------
    # Load workflow
    # -----------------------------------

    with open("workflows/workflow.json", "r", encoding="utf-8") as f:
        workflow = json.load(f)

    # -----------------------------------
    # Inject prompts
    # -----------------------------------

    # Positive prompt node
    workflow["6"]["inputs"]["text"] = prompt

    # Negative prompt node
    workflow["7"]["inputs"]["text"] = negative_prompt

    # Random seed
    workflow["3"]["inputs"]["seed"] = random.randint(1, 10**15)

    # -----------------------------------
    # Debug Prints
    # -----------------------------------

    print("\n========================")
    print("🎬 POSITIVE PROMPT:\n")
    print(prompt)

    print("\n🚫 NEGATIVE PROMPT:\n")
    print(negative_prompt)
    print("========================\n")

    # -----------------------------------
    # Send workflow to ComfyUI
    # -----------------------------------

    response = requests.post(
        f"{COMFY_URL}/prompt",
        json={"prompt": workflow}
    )

    response_data = response.json()

    prompt_id = response_data["prompt_id"]

    print(f"🆔 Prompt ID: {prompt_id}")

    # -----------------------------------
    # Wait for generated image
    # -----------------------------------

    max_wait = 1800
    waited = 0

    while waited < max_wait:

        try:
            result = requests.get(
                f"{COMFY_URL}/history/{prompt_id}"
            ).json()

            if prompt_id in result:

                outputs = result[prompt_id].get("outputs", {})

                for node_id in outputs:

                    images = outputs[node_id].get("images", [])

                    if images:

                        img = images[0]

                        filename = img["filename"]

                        subfolder = img.get("subfolder", "")

                        comfy_path = os.path.join(
                            COMFY_OUTPUT_FOLDER,
                            subfolder,
                            filename
                        )

                        # Ensure output folder exists
                        os.makedirs("output", exist_ok=True)

                        # Copy generated image
                        shutil.copy(
                            comfy_path,
                            FINAL_IMAGE_PATH
                        )

                        print(f"✅ Image saved: {FINAL_IMAGE_PATH}")

                        return FINAL_IMAGE_PATH

        except Exception as e:
            print(f"⚠️ Waiting... {e}")

        time.sleep(2)

        waited += 2

        print(f"⏳ Waiting for image... {waited}s")

    raise Exception("❌ Image generation failed (timeout)")