# Final Year Project Meeting Minutes

## Initial Meeting - 12 October 2022

*With Dr. Yuanlin Gu*

In this meeting, I proposed my initial idea for the project to my project supervisor, Dr. Yuanlin Gu. I discussed the intricacies of the idea, such as multiple 
different routes I could take with the project. Dr. Gu verbally approved my proposal.

Tasks after meeting:

- Complete Milestone 01 of getting signed approval from supervisor.
- Continue brainstorming ideas for the project.
- Begin to plan a roadmap for the project.
- Initialize important tasks, such as GitHub repository and Kanban board.

## Meeting 01 - 01 November 2022

*With Dr. Yuanlin Gu*

In this meeting, I discussed my roadmap that I had begun planning since the initial meeting. We also discussed the data collection aspect of the project, since the
current available data for current bus stops and routes is lackluster. Due to this, we concluded that I should manually collect the datapoints I desired.

Tasks after meeting:

- Manually collect data from coordinates using publically available documents and personal knowledge of the city.
- Begin testing algorithms as soon as possible in order to have solid foundation for the creation of the bus routes.
- Find resources to use in report.

## Meeting 02 - 08 November 2022

*With Dr. Yuanlin Gu*

In this meeting, Dr. Gu approved Milestone 02, which was the official Project Proposal. We talked through the dataset that I collected and Dr. Gu suggested areas of
improvement within the dataset and how these areas could benefit me in the future.

Tasks after meeting:

- Implement scores for each bus stop (if deemed useful) for the algorithm to have incentive to go to hotspots.
- Evaluate collected dataset.
  - Any possible reductions from the dataset?
  - Compare to other similar datasets, if possible.

## Meeting 03 - 15 November 2022

*With Dr. Yuanlin Gu*

In this meeting, we discussed additional features of comparison with existing bus routes in a European city of similar size, both geographically and population-wise.
This could be beneficial in the report.

Tasks after meeting:

- Use existing bus routes of a similar sized city in Europe to train algorithm to determine optimal number of bus routes for my system.
  - Can also use as comparison in final outcome.

## Meeting 04 - 22 November 2022

*With Dr. Yuanlin Gu*

In this meeting, I notified Dr. Gu of my algorithm implementation and testing. Dr. Gu introduced the idea of utilizing more complex algorithms than I have used before,
but instructed me to focus on the ones I know first to get a solid foundation to build from.

Tasks after meeting:

- Test algorithms we have already used, such as Dijkstra's Algorithm and A*.
- Also broaden horizons to include new algorithms after first step is done.
  - More advanced algorithms and techniques can be applied after the upcoming winter break.

## Meeting 05 - 29 November 2022

*Skipped due to illness.*

## Meeting 06 - 06 December 2022

*With Dr. Yuanlin Gu*

In this meeting, I displayed to Dr. Gu my prototype of testing algorithms, updated him with my plans for further testing, and introduced the idea for an interactive
website that can be deployed at the end, based on an example I found in my research.

Tasks after meeting:

- Use a function or loop to calculate straight-line distances from coordinates.
- Can use an algorithm to determine the number of routes.
  - Can even propose new roads for the city to build that would be beneficial to transport.
- Can use natural city subsections to group bus stop locations.

## Winter Break

No meetings occurred during Winter Break, but I continued to work on the project periodically.

## Meeting 07 - 26 January 2023

*With Dr. Yuanlin Gu*

In this quick meeting, Dr. Gu updated me on the updated guidelines for the Milestone 03 Mid-Project Review submission that is due in the upcoming week. We discussed
availability as well as general progress.

Tasks after meeting:

- Complete guidelines for Milestone 03 and be prepared to present to Dr. Gu and Mr. Ahmad.
- Create a meeting on Microsoft Teams so both can attend.
- Prepare presentation for meeting.

## Meeting 08 - 02 February 2023

*With Dr. Yuanlin Gu and Mr. Mohammad Ahmad*

In this meeting, I introduced my project to Mr. Mohammad Ahmad, my secondary marker, and we went over my progress thus far. We also discussed my progress on the report
and feedback was given. Mr. Ahmad approved my project and my progress thus far, and Milestone 03 was completed and submitted.

Tasks after meeting:

- Continue working on report, as the deadline approaches faster than it seems.
- Find solution to algorithm not working properly.
- Continue developing the map visualization of the paths.

## Meeting 09 - 07 February 2023

*With Dr. Yuanlin Gu*

In this meeting, I discussed in specifics the issue that I was having with my algorithm. In short, the A* algorithm I was using was not capable of displaying more
than 10 nodes in any given path. Dr. Gu suggested I move away from this specific implementation because it is extremely difficult to micromanage others' code and
try to fix things that you do not know the inner workings of completely.

Tasks after meeting:

- Take a short time trying to fix the current code.
- Research alternatives, A* algorithm or alternative.
- Continue developing the map visualization of the paths.

## Meeting 10 - 14 February 2023

*Skipped due to COVID-19.*

## Meeting 11 - 21 February 2023

*With Dr. Yuanlin Gu*

In this meeting, I discussed my progress with the algorithm development. After multiple attempts to fix the issues in my old implementation of the A* algorithm, I
decided to move away from it and research alternatives. Ultimately, I found that Dijkstra's algorithm worked perfectly, and I just needed to change the syntax of the
adjacency list. I also updated Dr. Gu on my progress with the map visualizations and how I found an API to implement driving routes on the map, not just waypoints
from coordinate to coordinate. Additionally, we discussed next steps for me since I overcame the biggest hurdle thus far.

Tasks after meeting:

- Test algorithm using multiple different source and destination nodes to determine best routes.
- Apply results to map visualization.
- Create basic website to host the interactive map visualization.
