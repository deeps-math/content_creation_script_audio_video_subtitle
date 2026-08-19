from tools.image_generator import generate_single_image
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# -----------------------------------
# SCENES
# -----------------------------------

# -----------------------------------
# SCENES
# -----------------------------------

# -----------------------------------
# SCENES
# -----------------------------------

SCENES = {

    "rain":
    """
    rainy window at night,
    blurred city lights outside,
    warm orange bokeh lights,
    deep blue cinematic shadows,
    realistic rain droplets on glass,
    emotional loneliness,
    cinematic heartbreak atmosphere,
    analog film photography,
    moody reflections,
    shallow depth of field,
    realistic textures,
    volumetric lighting,
    cozy darkness,
    film grain,
    emotional storytelling composition,
    empty emotional space for poetry text
    """,

    "message":
    """
    old phone on wooden table beside rainy window,
    unread messages glowing softly,
    dark red rose nearby,
    blurred warm city lights outside,
    emotional cinematic realism,
    realistic rain droplets,
    heartbreak atmosphere,
    moody reflections,
    analog film photography,
    shallow depth of field,
    warm orange glow,
    deep shadows,
    realistic textures,
    cozy darkness,
    vintage sadness aesthetic
    """,

    "goodbye":
    """
    lonely figure walking away in rain at night,
    blurred street lights,
    wet road reflections,
    emotional cinematic realism,
    foggy atmosphere,
    heartbreak aesthetic,
    analog photography,
    moody shadows,
    film grain,
    warm orange lights against blue darkness,
    realistic rainy environment,
    emotional storytelling composition,
    empty emotional composition
    """,

    "memory":
    """
    scattered photographs on wooden floor,
    warm lamp light,
    emotional nostalgia,
    cinematic sadness,
    vintage aesthetic,
    shallow depth of field,
    analog photography,
    dusty atmosphere,
    realistic textures,
    soft grain texture,
    warm cinematic glow,
    emotional storytelling,
    melancholic mood
    """,

    "overthinking":
    """
    person awake at night beside rainy window,
    moonlight shadows,
    emotional loneliness,
    cinematic realism,
    cozy darkness,
    soft film grain,
    melancholic atmosphere,
    vintage emotional photography,
    warm orange lights outside,
    deep blue shadows,
    realistic room textures,
    emotional storytelling composition
    """,

    "window":
    """
    rainy window with blurred city lights,
    emotional loneliness,
    cozy darkness,
    cinematic atmosphere,
    analog photography,
    warm orange bokeh lights,
    moody reflections,
    heartbreak aesthetic,
    realistic rain droplets,
    shallow depth of field,
    emotional realism,
    vintage cinematic mood
    """,

    "heartbreak":
"""
rainy window at night,
water droplets running down glass,
warm orange city lights glowing outside,
dark red rose on wet wooden table,
phone with unread messages beside rose,
realistic rain reflections,
emotional loneliness,
cinematic heartbreak atmosphere,
deep blue shadows,
warm golden highlights,
soft fog,
realistic wet textures,
analog film photography,
melancholic storytelling,
empty emotional space for poetry text
""",

    "lost_love":
    """
    lonely rainy room at night,
    blurred warm street lights outside,
    dark red rose beside old phone,
    emotional loneliness,
    cinematic sadness,
    realistic photography,
    deep shadows,
    warm orange glow,
    soft blue tones,
    rain on window,
    film grain,
    analog photography aesthetic,
    heartbreak mood,
    shallow depth of field,
    realistic textures,
    emotional storytelling composition
    """,

   "first_love":
"""
empty classroom after school,
rain outside classroom window,
warm sunset light through dusty windows,

two notebooks touching softly,
single dark red rose placed beside notebook,
rose visible in foreground,

empty desks and chairs,
faded handwritten notes,

nostalgic emotional atmosphere,
cinematic realism,
warm golden lighting,
soft shadows,

analog film photography,
shallow depth of field,
dreamy emotional storytelling,

subtle dust particles in sunlight,
melancholic first love aesthetic,
realistic photography,

warm orange glow,
rain reflections,
emotional loneliness
""",

    "love":
    """
    couple silhouette near rainy window,
    warm golden lights,
    emotional romantic atmosphere,
    cinematic photography,
    soft shadows,
    analog film aesthetic,
    realistic emotional intimacy,
    shallow depth of field,
    warm cozy lighting,
    realistic textures,
    dreamy romantic mood,
    emotional storytelling composition
    """,

    "alone":
    """
    lonely person sitting in dark room,
    rainy atmosphere,
    warm city lights outside window,
    emotional loneliness,
    cinematic realism,
    analog film photography,
    soft shadows,
    deep blue tones,
    realistic emotional atmosphere,
    film grain,
    shallow depth of field,
    heartbreak aesthetic
    """,

   "empty_classroom":
"""
empty classroom after school hours,
warm sunset light through dusty windows,

abandoned notebook on wooden desk,
single dark red rose on wooden desk,
rose visible in foreground,

handwritten love letter partially visible,

lonely nostalgic atmosphere,
cinematic emotional realism,

soft golden sunlight,
dust particles floating in air,

analog film photography,
shallow depth of field,

melancholic first love aesthetic,
warm orange glow,

realistic classroom textures,
emotional storytelling composition,

quiet heartbreak mood,
vintage cinematic feeling,

empty emotional space for poetry text
""",

    "train":
    """
    lonely train platform at night,
    warm station lights,
    emotional loneliness,
    cinematic atmosphere,
    rain reflections on ground,
    realistic photography,
    analog film aesthetic,
    deep shadows,
    shallow depth of field,
    melancholic storytelling,
    emotional realism
    """,

    "ocean":
    """
    person standing near ocean at sunset,
    emotional loneliness,
    cinematic realism,
    warm sunset glow,
    soft waves,
    nostalgic atmosphere,
    analog photography,
    realistic textures,
    emotional storytelling composition,
    dreamy melancholic aesthetic
    """,

    "city":
    """
    lonely silhouette in crowded city at night,
    blurred neon lights,
    emotional isolation,
    cinematic realism,
    rain reflections,
    analog film photography,
    warm orange and blue tones,
    moody atmosphere,
    shallow depth of field,
    emotional storytelling,
    realistic city textures
    """,

    "road":
    """
    lonely person walking on foggy road at night,
    street lights glowing softly,
    emotional sadness,
    cinematic realism,
    analog film aesthetic,
    rain reflections,
    deep shadows,
    warm orange highlights,
    emotional storytelling atmosphere,
    realistic photography
    """
}


# -----------------------------------
# DETECT SCENE
# -----------------------------------

def get_scene_from_topic(topic):

    topic = topic.lower()

    if "message" in topic or "text" in topic or "reply" in topic:
        return SCENES["message"]

    elif "goodbye" in topic or "leave" in topic:
        return SCENES["goodbye"]

    elif "memory" in topic or "photo" in topic:
        return SCENES["memory"]

    elif "sleep" in topic or "overthinking" in topic:
        return SCENES["overthinking"]

    elif "window" in topic:
        return SCENES["window"]

    elif "heartbreak" in topic or "broken" in topic:
        return SCENES["heartbreak"]

    elif "lost love" in topic or "lost" in topic:
        return SCENES["lost_love"]
    
    elif "classroom" in topic or "school" in topic:
        return SCENES["empty_classroom"] 
    
    elif "first love" in topic:
        return SCENES["first_love"]
    



    elif "love" in topic or "romance" in topic:
        return SCENES["love"]

    elif "alone" in topic or "lonely" in topic:
        return SCENES["alone"]

   

    elif "train" in topic or "station" in topic:
        return SCENES["train"]

    elif "ocean" in topic or "sea" in topic:
        return SCENES["ocean"]

    elif "city" in topic or "crowd" in topic:
        return SCENES["city"]

    elif "road" in topic or "walking" in topic:
        return SCENES["road"]

    return SCENES["rain"]


# -----------------------------------
# WATERMARK
# -----------------------------------

def add_watermark(image_path):

    text = "Subscribe for more @SoulEmotionsUnspoken"

    img = Image.open(image_path).convert("RGBA")

    width, height = img.size

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(
        "C:/Windows/Fonts/georgia.ttf",
        int(width * 0.032)
    )

    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2

    y = height - text_height - 18

    # soft shadow
    draw.text(
        (x + 1, y + 1),
        text,
        font=font,
        fill=(0, 0, 0, 120)
    )

    # main
    draw.text(
        (x, y),
        text,
        font=font,
        fill=(255, 240, 220, 255)
    )

    final_path = image_path.replace(
        ".png",
        "_watermarked.png"
    )

    img.save(final_path)

    return final_path


# -----------------------------------
# WRAP TEXT
# -----------------------------------

def wrap_text(draw, text, font, max_width):

    words = text.split()

    lines = []

    current_line = ""

    for word in words:

        test_line = current_line + word + " "

        bbox = draw.textbbox(
            (0, 0),
            test_line,
            font=font
        )

        text_width = bbox[2] - bbox[0]

        if text_width <= max_width:

            current_line = test_line

        else:

            lines.append(current_line.strip())

            current_line = word + " "

    lines.append(current_line.strip())

    return lines


# -----------------------------------
# ADD QUOTE TEXT
# -----------------------------------

def add_quote_text(image_path):

    with open(
        "memory/title.txt",
        "r",
        encoding="utf-8"
    ) as f:

        title = f.read().strip()

    with open(
        "memory/script.txt",
        "r",
        encoding="utf-8"
    ) as f:

        script = f.read().strip()

    img = Image.open(image_path).convert("RGBA")

    width, height = img.size

    draw = ImageDraw.Draw(img)

    # -----------------------------------
    # FONTS
    # -----------------------------------

    title_font = ImageFont.truetype(
        "C:/Windows/Fonts/BRUSHSCI.TTF",
        int(width * 0.065)
    )

    script_font = ImageFont.truetype(
        "C:/Windows/Fonts/georgia.ttf",
        int(width * 0.055)
    )

    # -----------------------------------
    # TITLE PAPER
    # -----------------------------------

    paper_width = int(width * 0.72)
    paper_height = 120

    paper = Image.new(
        "RGBA",
        (paper_width, paper_height),
        (210, 190, 165, 235)
    )

    paper_draw = ImageDraw.Draw(paper)

    # subtle texture noise
    for _ in range(1200):

        x_noise = random.randint(0, paper_width - 1)
        y_noise = random.randint(0, paper_height - 1)

        alpha = random.randint(10, 35)

        paper_draw.point(
            (x_noise, y_noise),
            fill=(120, 90, 60, alpha)
        )

    paper = paper.filter(
        ImageFilter.GaussianBlur(0.3)
    )

    # slight tilt
    paper = paper.rotate(
        -4,
        expand=True
    )

    # paste position
    paper_x = 40
    paper_y = 35

    img.paste(
        paper,
        (paper_x, paper_y),
        paper
    )

    draw = ImageDraw.Draw(img)

    # -----------------------------------
    # TAPE
    # -----------------------------------

    tape = Image.new(
        "RGBA",
        (50, 26),
        (235, 235, 235, 110)
    )

    tape = tape.rotate(
        6,
        expand=True
    )

    img.paste(
        tape,
        (65, 20),
        tape
    )

    # -----------------------------------
    # TITLE TEXT
    # -----------------------------------

    title_lines = wrap_text(
        draw,
        title,
        title_font,
        width * 0.58
    )

    y = 55

    for line in title_lines:

        bbox = draw.textbbox(
            (0, 0),
            line,
            font=title_font
        )

        line_width = bbox[2] - bbox[0]

        x = 70

        # subtle shadow
        draw.text(
            (x + 1, y + 1),
            line,
            font=title_font,
            fill=(0, 0, 0, 35)
        )

        # title
        draw.text(
            (x, y),
            line,
            font=title_font,
            fill=(35, 20, 18, 255)
        )

        y += int(title_font.size * 1.0)

    # -----------------------------------
    # SCRIPT
    # -----------------------------------

    script_lines = []

    sentences = script.split("...")

    for sentence in sentences:

        sentence = sentence.strip()

        if sentence:

            wrapped = wrap_text(
                draw,
                sentence,
                script_font,
                width * 0.72
            )

            for line in wrapped:

                script_lines.append(line)

            script_lines.append("")
            script_lines.append("")

    y = int(height * 0.27)

    line_height = int(script_font.size * 1.55)

    for line in script_lines:

        if line == "":

            y += int(line_height * 0.65)

            continue

        bbox = draw.textbbox(
            (0, 0),
            line,
            font=script_font
        )

        line_width = bbox[2] - bbox[0]

        x = (width - line_width) // 2

        # shadow
        draw.text(
            (x + 1, y + 1),
            line,
            font=script_font,
            fill=(0, 0, 0, 90)
        )

        # poetic text
        draw.text(
            (x, y),
            line,
            font=script_font,
            fill=(255, 242, 230, 255)
        )

        y += line_height

    # -----------------------------------
    # SAVE
    # -----------------------------------

    final_path = image_path.replace(
        ".png",
        "_final.jpg"
    )

    img = img.convert("RGB")

    img.save(
        final_path,
        quality=95
    )

    return final_path
# -----------------------------------
# MAIN AGENT
# -----------------------------------

def run_image_agent(topic):

    scene = get_scene_from_topic(topic)

    prompt = f"""
{scene},

masterpiece,
best quality,
ultra realistic photography,
cinematic emotional realism,

rain droplets on glass,
water dripping on window,
wet reflections,
realistic wet surfaces,

warm orange bokeh lights,
golden cinematic glow,
warm highlights,
deep blue shadows,
dark moody atmosphere,

visible dark red rose placed on desk,
single realistic red rose clearly visible,
rose near notebook,
rose illuminated by warm cinematic lighting,
wet rose petals,
rose visible in foreground,
subtle emotional symbolism,

emotional storytelling composition,
heartbreak aesthetic,
nostalgic atmosphere,

analog film photography,
35mm film look,
Kodak cinematic colors,
subtle film grain,

volumetric lighting,
soft fog,
shallow depth of field,
high contrast shadows,

realistic textures,
hyper realistic lighting,
cozy darkness,

instagram viral aesthetic,
tiktok emotional aesthetic,

empty emotional space for poetry text
"""

    negative_prompt = """
worst quality,
low quality,
anime,
cartoon,
painting,
drawing,
cgi,
3d render,

bright daylight,
flat lighting,
oversaturated colors,
cheap aesthetic,
plastic textures,

flower bouquet,
multiple roses,
oversized rose,
fake flowers,

deformed body,
extra fingers,
bad anatomy,

duplicate objects,
extra limbs,

low realism,
washed colors,
low contrast,

text,
watermark,
logo
"""

    print("\n🎬 GENERATED PROMPT:\n")
    print(prompt)

    image_path = generate_single_image(
        prompt,
        negative_prompt
    )

    watermarked = add_watermark(
        image_path
    )

    final_image = add_quote_text(
        watermarked
    )

    print(f"\n✅ Final image: {final_image}")

    return final_image


# -----------------------------------
# TEST
# -----------------------------------

if __name__ == "__main__":
    topic = " first love in classroom"

    final_image =run_image_agent(topic)

    #image_path = "output/image.png"

    #watermarked_image = add_watermark(
      #  image_path
   # )

    #final_image = add_quote_text(
   #     watermarked_image
    #)

    print(final_image)