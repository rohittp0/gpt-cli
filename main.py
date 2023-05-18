from transformers import pipeline, set_seed


def main():
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)

    context = []

    while True:
        prompt_text = input("Write a prompt: ")
        context.append(f"Prompt: {prompt_text}\nReply: ")

        result = generator("\n".join(context), max_length=50, num_return_sequences=1)[0]
        result = result['generated_text']

        new = result.split("Reply: ")[-1]
        context.append(new)

        print(new)


if __name__ == "__main__":
    main()
