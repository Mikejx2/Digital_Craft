coin = 0

print(f"You have {coin} coins.")

answer = input("Do you want another? ")



while answer.lower() == "yes":
    # if another.lower() == "yes":
        coin += 1
        print(f"You have {coin} coins.")
        answer = input("Do you want another? ")
        


while answer.lower() == "no":
    print("Bye")
    break


