#!/bin/bash

function openFirstProject() {

	comand cd $HOME/Documents/PythonNotes || echo "Your folder isn't here anymore" && return

	sublime FirstProject.py
	open ./FirstInstructions.html
}

function saveFirstProject() {
	command cd $HOME/Documents/PythonNotes || echo "Your folder isn't here anymore" && return
	git status
	git add $HOME/Documents/PythonNotes/FirstProject.py
	git commit -m "First project"
	git push origin master

	echo "Your work has been saved"

}

function testCode() {
	command cd $HOME/Desktop/PythonHomework
	python FirstProject.py
}

getStarted