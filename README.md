# Sainsmart Relay GUI

## Setup
* Download and install Python 3.7.8 if not already installed, later revisions are not supported!
* Install the latest version of pip if not already installed
* Install required modules for your OS:

        pip install -r requirements-base.txt
        pip install -r requirements-windows.txt

## Build
* Create a Python Virtual Environment:

        python -m virtualenv --python "C:\Program Files\Python37\python.exe" venv

* Enable script execution if necessary:

        Set-ExecutionPolicy Bypass -Scope Process -Force

* Activate the virtual environment:

        .\venv\Scripts\activate.ps1

* Install required virtual environment modules for your OS:

        pip install -r requirements/base.txt
        pip install -r requirements/windows.txt

* Run the project locally:

        fbs run

* Deactivate virtual environment:

        deactivate

## Install
* Activate the virtual environment:

        .\venv\Scripts\activate.ps1

* Lock Changes for Distribution Package:
    * Install Requested Packages

                fbs freeze

* Create Installer:
    * Install Requested Packages

                fbs installer

## Usage
* Install Distributable Application

### Configuration
#### Modes
* Ethernet

#### Relays
* 16 Channel

## Credit
