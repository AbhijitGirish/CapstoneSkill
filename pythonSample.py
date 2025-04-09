def main():
    """
    Main function to demonstrate Git concepts using print statements that ask questions.
    """
    print("Test your Git knowledge!\n")

    questions = [
        ("What is Git?", "b) A version control system"),
        ("What is a repository?", "c) A directory with version control info"),
        ("Which command creates a repo?", "c) git init"),
        ("What is the staging area?", "c) Select changes for commit"),
        ("Which command adds to staging?", "a) git add"),
        ("What does `git commit` do?", "c) Records changes locally"),
        ("What is a commit message?", "b) Short description of changes"),
        ("Which command shows commit history?", "c) git log"),
        ("What is a branch?", "b) A pointer to a specific commit"),
        ("Which command creates a branch?", "c) git branch"),
    ]

    for q, correct_answer in questions:
        print(f"{q}\n{correct_answer}\n")

    print("Thanks for the quiz!")

if __name__ == "__main__":
    main()
