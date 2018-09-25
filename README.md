# Data Science Lab

Team members
<ul>
   <li>Jerry Yang</li>
   <li>Zhaofeng Liang</li>
   <li>Daniel Diamont</li>
</ul>
</p>

# Installation

## Installing the repository for the first time
<p>
Clone the repository.
</p>

```bash
$ git clone https://github.com/danieldiamont/DataScienceLab.git
```

<p>
Navigate into the cloned repository.
</p>

```bash
$ cd DataScienceLab
```

<p>
Set up a python virtual environment. 
(There are several ways to do this, my favorite is below)
</p>

```bash
$ virtualenv -p python3 .env
```

This sets up the environment under the name `.env` which is not descriptive, but keeps me from having to remember how to activate all my different environments. Feel free to install the environment under whatever name you wish, so long as you add the environment name to the .gitignore file in the appropriate place.

### Virtual Environment Activation, Installation of Dependencies, and Usage

<p>
Next activate the environment, and install all the python dependencies via the requirements file. When the environment is active it will display to the left of the prompt, as shown below.
</p>

```bash
$ source .env/bin/activate
(.env) $ sudo pip install -r requirements
```

<p> 
If you install additional libraries, please update the requirements and add the modified file to your commit.
</p>

```bash
$ cd /<ROOT_PATH>/DataScienceLab
$ pip freeze > requirements
```

<p>
When finished with the repository or environment, you can deactivate it with the simple command deactivate.
</p>

```bash
(.env) $ deactivate
$ 
```

## Updating the documentation

To update any README's, just open the .md file in your favorite text editor. You can render markdown files in your local browser to ensure they look the way you want by activating your environment, and running

```bash
$ grip <readme name>
```

