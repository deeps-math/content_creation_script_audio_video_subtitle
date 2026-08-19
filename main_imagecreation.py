from agents.image_agent import run_image_agent
if __name__ == "__main__":
    topic = "waiting for someone who never comes"

    final_image = run_image_agent(topic)

    print(final_image)