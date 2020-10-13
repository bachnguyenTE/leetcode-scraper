**Program**: leetcode-scraper  
**Copyright   2020, All Rights Reserved**

## Compilation
> **Language**: Python  
**Version**: 3.8  
**Dependencies**: selenium
**Platform**: Windows

## Procedure and Implementation
> Program is presented as a single `webscrape.py` executable. Execute with all dependencies.
> Dynamic webscraping using Selenium as core scraping library.

**Procedure**
- The program login to Leetcode with a dummy account that solved the algorithm of the dataset.
- Empty directories are created to store the dataset.
- The program then checks for the two graph type in the submission review page, runtime and memory graph.
	- Search and locate the coordinate of the graph within the webpage,
	- Initialize the directories to save the scraped data,
	- Using Selenium cursor location, move the cursor with a loop and search for a pop-up box,
    - The pop-up indicates whether there is a bar of the graph in said location,
	- When a pop up is found, click on the element, which is a bar graph,
    - The sample code within the modal window that opens thereafter is stored into a .txt file and outputed to the directories.
 
**Implementation details and cautions**
- During login, the program must wait for the web button to finish rendering.
- For every click action on the bar graph to open the modal window, the process waits for several seconds to let the webpage fetch the sample code from the server.
- If a modal window containing the sample code is opened, ESC is pressed to exit the window (previously clicked the exit button, but there are cases where the exit button does not render).
- Loop iteration increment by several pixels at once due to runtime constraints; this skips over many data points but greatly improves runtime (as data collection is reduced, sample size is still sufficient).
