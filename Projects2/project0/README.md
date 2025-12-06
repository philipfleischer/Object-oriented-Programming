# Project 0
First project in IN1910 about testing with pytest and git

Repository URL: https://github.uio.no/IN1910/H25_project0_philipef

To run the project:
    pytest test_calculator.py
    
## Authors

- Philip Elias Fleischer (philipef@ifi.uio.no)


## Comments
Looking back, I realize that I ended up with far too many commits. This happened because I misunderstood how I should structure my workflow, and I didn’t really think about it until the project was finished. In particular, exercise 6 caused me some trouble, and I had to make several changes afterwards, which led to additional commits.

In retrospect, I spent too much time making commits that were too small. I found it oddly satisfying to commit frequently, but this only made the history more cluttered than useful. At first, I thought this approach would give me a better overview, but after lecture 4 I understood that too many commits can make the history difficult to navigate effectively. I recognize this mistake and will avoid it in the future.

Part of the reason was that I interpreted the lectures as if one should commit before every test run of the program. In hindsight, I should have reflected more on why this was done during the lectures. I believe the point was to highlight the importance of committing regularly, but in my case this became excessive. This is, of course, my own responsibility, and I take it as a learning point.

When I ran mypy test_calculator.py, I got the following error message:
test_calculator.py:1: error: Cannot find implementation or library stub for module named "pytest".

I discussed this with my group teacher, who assured me that this was not a problem. Therefore, I didn’t make any changes and left it as is.

Finally, I chose not to do exercise 9. The reason is that I found the mathematical complexity far beyond what I could reasonably handle on my own within the time frame, so I prioritized the mandatory exercises instead.
