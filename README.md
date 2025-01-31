# [WIP!] Stepgen
The goal of this project is to implement an autostepper program made to support quick generation of stepfiles from playlists

This project is expected to progress in several stages. 

* First, I would like to create, using simple heuristics, stepfiles that activate random arrows for each note. Even this is not a simple task, but should be doable. This includes detecting the BPM of a song, calculating the necessary offset, and then detecting when a new note is played. A note has a specific **start time**, **frequency**, and **duration**, which are relevant to how a note should be represented going into a stepfile. 
  
![Short Time Fourier Transform of a Music File, Showing Rough Display of Notes](STFT_test1.png)
The above image is an example of preliminary testing. It's possible to run a "Short-Time Fourier Transform" on the audio signal to split individual results into tracks and frequencies. However, there are several parameters to be tuned. For this particular song, it works decently, but for another track with the same parameters, it might look like the following:

* Second, I would like to add on the possibility to select which set of patterns are to be used to improve the diversity of the resulting stepfiles.
* Third, I would like to look at deep learning approaches to consider what can be improved upon. This is the most vague requirement and may require significant research and data collection.
  

# Inspiration:
This project has been suggested many times. It seems like there is a demand for auto-generated stepfiles. Personally, I would like the ability to take a playlist of my songs and have a task run that converts this into "decent" (probably difficult to make completely optimal) stepfiles for me to play with.
* [Dance Dance Convlution](https://github.com/chrisdonahue/ddc)
* [AutoStepper](https://github.com/phr00t/AutoStepper)

Unfortuntately, many times such projects have staled and not been completed
* [StepMania Tools](https://github.com/jjaquinta/StepManiaTools)
* [MIDI to Stepfile](https://www.reddit.com/r/Stepmania/comments/5n0snz/progress_on_midi_to_stepfile/)

> Disclaimer : Currently in dev. Progress below

# Tips:

The following document provides some inspiration on note pattersn and describes how to calculate the offset for a stepfile, if done manually.
https://docs.google.com/document/u/0/d/1Yb9hiewZFs27F3mB6V3reiRBA3E00zb_xfjGVcsnYhg/mobilebasic#h.tv62oe7zl3qz



# How to run
* Clone the repo
  ```shell
  git clone https://github.com/bradleeharr/Stepgen.git
  cd Stepgen
  ```
* Make a virtual env
  ```shell
  python -m venv .venv`
  ```
* Activate the virtual env
  ```shell
  .venv/scripts/activate
  ``` 
* Install requirements
  ```
  pip install -r requirements.txt
  ``` 



# Checklist

### Pattern-Based
* - [x] Song BPM (Rough)
* - [x] FFT of Song
* - [ ] Time Offset
   * - [ ] Compare with Audacity/Manual Time Offset 
* - [ ] Song BPM (More Exact)
* - [ ] Song Speed
* - [ ] Song Length
* - [ ] Analyze Stepfiles
* - [x] Output to Stepfile (headers)
* - [ ] Output Quarter Notes to StepFile
* - [ ] Add patterns
  * - [ ] 8ths   
  * - [ ] 16ths
  * - [ ] Basic Patterns
    *  - [ ]  Candles
    *  - [ ]  Jumps
    *  - [ ] Chain Jumps
    *  - [ ] Step Jumps
    *  - [ ] Freeze Arrows / Holds
    *  - [ ] Drills
    *  - [ ] Jacks
    *  - [ ] Gallops
  * - [ ] Determine when and where to place each type of patterns by default
  * - [ ] Determine crieteria for config -- user can select areas wth Jumps or perhaps detail areas with higher musical intensity to be considered Drills
  * - [ ] Complex Patterns
    *  - [ ]  Crosses
    *  - [ ]  Double Steps
    *  - [ ]  Spins
    *  - [ ]  Sub-Patterns
    *  - [ ]  Triples/Triplets
    *  - [ ]  Fourthlets

* - [ ] Analyze FFT of songs to generate beats
* - [ ] Review [AutoStepper](https://github.com/phr00t/AutoStepper)
* - [ ] Generate Background Animations using some Music Visualizer

### NN-Based
* - [ ] Gather Stepfiles
  - [ ] Create DNN
  - [ ] Test first approach
 
* - [ ] Review [DanceDanceConvolution](https://github.com/chrisdonahue/ddc)






##### Would be cool to add an option for lyrics popping up
##### default.lua script seems like you can animate backgrounds and stuff
##### Visualizer would be an interesting additiojn
##### Manim for animations maybe?
