# CS-340 Client/Server Development

Grazioso Salvare Animal Rescue Dashboard

## About This Project

This repository contains my Project Two work for CS-340 at Southern New Hampshire University. The project is a full stack dashboard built for Grazioso Salvare, a company that trains rescue animals. It sits on top of the Austin Animal Center Outcomes data set and lets a non technical user filter roughly ten thousand shelter records down to the dogs that fit a specific search and rescue profile, without writing a single query.

The application follows the Model View Controller pattern. MongoDB holds the data, a Python CRUD module handles all database access, and Dash provides both the interface and the callback logic that ties the widgets together.

## Contents

| File | Description |
|---|---|
| `ProjectTwoDashboard.ipynb` | The complete dashboard: rescue type filters, interactive data table, breed distribution pie chart, and geolocation map |
| `CRUD_Python_Module.py` | The `AnimalShelter` class from Project One, providing create, read, update, and delete operations against MongoDB |
| `Project Two README - Luca Formento.docx` | The written Project Two component, including screenshots of the working dashboard |

## Functionality

Selecting a rescue type radio button sends a MongoDB query through the CRUD module and repopulates the data table with the matching dogs. Because the pie chart and the map both listen to the table rather than to the radio buttons directly, they update automatically whenever the table changes, and they also respond to sorting and native filtering performed inside the table itself.

The three rescue profiles filter on breed, sex, and age in weeks:

- **Water Rescue:** intact female dogs, 26 to 156 weeks
- **Mountain or Wilderness Rescue:** intact male dogs, 26 to 156 weeks
- **Disaster or Individual Tracking:** intact male dogs, 20 to 300 weeks

## Tools Used

**MongoDB** serves as the model. The shelter data is a flat export where each animal is a self contained record, which maps onto MongoDB's document model with no schema design or table joins required. What makes it especially useful with Python is that its documents are essentially JSON, and the PyMongo driver hands them back as native dictionaries. A query document, a returned record, and a Python dictionary are all the same shape, so there is no object relational mapping layer to write.

**Dash** provides the view and the controller. The entire interface is declared as Python objects and rendered as React components in the browser, so I built a browser based dashboard without writing any HTML, CSS, or JavaScript. Its reactive callback system is what chains the widgets together.

**Dash Leaflet** handles the geolocation map, **Plotly Express** handles the pie chart, and **pandas** reshapes query results in between the database and the widgets.

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

The CRUD module was the clearest lesson in this for me. Building it as a standalone class in Project One meant that by the time I got to Project Two, I never had to think about database connections again. Every filter in the dashboard is just a query dictionary handed to `read()`. If I had scattered PyMongo calls throughout the dashboard code instead, changing something like the connection string or the authentication method would have meant hunting through every callback to find them.

The big advantage was that it let me work in layers. I could build and verify the database access completely on its own, then build the interface on top of something I already trusted. When the dashboard broke, and it broke several times, I knew the problem was in the callback logic rather than the data layer, which narrowed the search a lot. I also kept the query construction separate from the callback that uses it, so each rescue type is its own small function returning a query document. Adding a fourth rescue type would mean writing one function and adding one line to a dictionary. That is the kind of thing I would not have bothered with a year ago, and it made a real difference here.

The module itself is not tied to this dashboard in any way. It only knows about a MongoDB collection and four operations. I could point it at a different collection and reuse it for a REST API, a command line tool for shelter staff to add intake records, or a scheduled script that syncs new outcome data. Honestly the more useful takeaway is the pattern rather than the file. Any project I do that touches a database is going to get a layer like this now.

### How do you approach a problem as a computer scientist?

I started with the data rather than the code, which is not what I would have done before this course. Before writing anything I imported the data set and spent time in the Mongo shell just querying it, checking what the field names actually were, whether `age_upon_outcome_in_weeks` came in as a number or a string, and how the breed values were formatted. That last one mattered more than I expected. The breed field contains entries like "Labrador Retriever Mix" as distinct values, so an exact match filter behaves very differently from what you might assume looking at the requirements on paper.

The difference from previous courses is that this one had a client with requirements rather than a spec that told me exactly what to build. Grazioso Salvare said they wanted to find dogs suited to water rescue. Translating that into a query with specific breed, sex, and age constraints, and then deciding whether to match breeds exactly or loosely, was a judgment call I had to make and defend. In earlier courses the correct output was usually defined for me. Here I had to decide what correct meant and be able to explain why.

I also built the dashboard in layers rather than all at once, which saved me a lot of debugging. Layout first, then the table with unfiltered data, then the filters, then the charts. Each piece got verified before the next one went on top of it. Going forward, the strategies I would carry into another client project are exploring the data before designing anything, isolating database access behind its own module, and asking clarifying questions about ambiguous requirements early instead of guessing and finding out at the end.

### What do computer scientists do, and why does it matter?

The way I see it, computer scientists take a problem someone has and turn it into something a machine can solve repeatedly and reliably. The valuable part is usually not the code. It is understanding the problem well enough to know what to build in the first place.

For Grazioso Salvare, the practical difference is time. Without this dashboard, finding candidate dogs across roughly ten thousand shelter records means either someone reading through spreadsheets by hand or someone on staff who knows how to write database queries. Both are slow, and the manual version is easy to get wrong. With the dashboard, a trainer who has never seen a query in their life clicks one radio button and gets the matching dogs, their locations on a map, and a breakdown of what breeds are available. That turns a research task into a few seconds of clicking.

The part I find genuinely interesting is that the work has a real outcome attached to it. These are animals that either get identified as rescue candidates or do not. Making that search faster and more reliable means more dogs actually get placed into training. That is a better reason to write good code than a grade is.


## Resources

- [MongoDB Documentation](https://www.mongodb.com/docs)
- [PyMongo Documentation](https://pymongo.readthedocs.io)
- [Dash Documentation](https://dash.plotly.com)
- [Dash Leaflet Documentation](https://www.dash-leaflet.com)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express)
- [pandas Documentation](https://pandas.pydata.org/docs)

Austin Animal Center. (2020). *Austin Animal Center Outcomes* [Data set]. City of Austin, Texas Open Data Portal. https://doi.org/10.26000/025.000001

---

Luca Formento | CS-340 Client/Server Development | Southern New Hampshire University
