import json

def main():
    data = []

    while True:
        input1 = input("")
        if input1 != "":
            input2 = input("")
            data.append({input1: input2})
        else:
            print("Json not found, exiting")
            with open("dumps.json", "w") as f:
                json.dump(data, f, indent=4)
            break

if __name__ == "__main__":
    main()