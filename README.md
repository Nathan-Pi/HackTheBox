# HackTheBox


# ** Git commit best practices - **
https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60

# **Ticket writing syntax - **

example: 

Feature: Refund item

Scenario: Jeff returns a faulty microwave
Given Jeff has bought a microwave for $100
And he has a receipt
When he returns the microwave
Then Jeff should be refunded $100

Gherkin follows a very specific syntax:

Scenario -> Given -> When -> Then
Scenarios: All the actions a user could take (including bad input)
GIVEN: Sets the context. What page are we on and what state are we in? Is the user an admin? Signed-in? Has created a campaign?
WHEN: What actions the user is performing. What event occurred?
THEN: What should the system do in response? What is the expected outcome?

** #Git branching good practices**
https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops

# HOW TO CREATE PULL REQUEST
1) Make sure you are on your branch with "git checkout <branch_name>
2) git fetch (fetch changes from main)
3) git merge main (merge your branch with main)
4) git add . (stage changes)
5) git commit -m "<message>" (commit changes)
6) git push origin <branch_name> (push changes to your branch)
7) Go to github, go to your branch and there will be a review and submit pull request button somewhere
