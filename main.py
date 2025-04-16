from pet import Pet

def main():
    buddy = Pet("Hannah")

    buddy.get_status()
    buddy.eat()
    buddy.sleep()
    buddy.play()
    buddy.get_status()

    buddy.train("roll over")
    buddy.train("sit")
    buddy.show_tricks()

if __name__ == "__main__":
    main()

