[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17989115)
# Lab2 - CIST 1600
Variables, assignment, numerical types, arithmetic operators

## Magic8Ball.py
Create a program that will allow the user to ask a question, then provide a random response like a Magic 8 Ball.

- A traditional Magic 8 Ball has 20 possible answers:
- As I see it, yes.
- Ask again later.
- Better not tell you now.
- Cannot predict now.
- Concentrate and ask again.
- Don’t count on it.
- It is certain.
- It is decidedly so.
- Most likely.
- My reply is no.
- My sources say no.
- Outlook not so good.
- Outlook good.
- Reply hazy, try again.
- Signs point to yes.
- Very doubtful.
- Without a doubt.
- Yes.
- Yes – definitely.
- You may rely on it.

You may select to use these or answers you have created. They key is that they are given a random answer to the question they ask.

How to create a list of possible answers:
```
answers = ["thing 1", "thing 2"] # Each item must be in quotes, separated by a comma.
```
Since we imported random at the top of our file, we can use the following code to select a random item from the list.
```
response = random.choice(answers)
```
---
## FutureTime.py
Create a program that asks the user for a number of hours and minutes, then computes the time it will be when those hours/minutes have passed based on the current time obtained from the system.

We have not yet talked about if statements or other control structures. You should be able to accurately get the future time using only mathematical operations discussed in Lecture 2.

#### Things to consider
- How do I get input from the user?
- Is this input in the correct data type?
  - How do I convert data types if it is not?
- 9 + 7 = 16... how do I convert to a 1-12 hour range without if statements?
- How do I use these variable so print info in the "HH:MM" format?

---

## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
Submit your work in GitHub Classroom
