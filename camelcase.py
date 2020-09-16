def camel_case (sentence):
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(" ", "")

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    message = "CAMMELCASE PROGRAM!!"
    stars = "*" * len(message)
    print(f"{stars}\n{message}\n{stars}")

def main():
    banner()
    print("\nThis program converts a sentence into one camelCase word.\n")
    sentence = input("Enter your sentence: ")
    output = camel_case(sentence)
    print(output)

if __name__ == '__main__':
    main()