# Stepgen
An autostepper program made to support quick generation of stepfiles from playlists


# Inspiration:
This project has been suggested many times. It seems like there is a demand for auto-generated stepfiles. Personally, I would like the ability to take a playlist of my songs and have a task run that converts this into "decent" (probably difficult to make completely optimal) stepfiles for me to play with.
* [Dance Dance Convlution](https://github.com/chrisdonahue/ddc)
* [AutoStepper](https://github.com/phr00t/AutoStepper)

Unfortuntately, many times such projects have staled and not been completed
* [StepMania Tools](https://github.com/jjaquinta/StepManiaTools)
* [MIDI to Stepfile](https://www.reddit.com/r/Stepmania/comments/5n0snz/progress_on_midi_to_stepfile/)


# Tips:
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
* - [ ] Song BPM (More Exact)
* - [ ] Song Speed
* - [ ] Song Length
* - [ ] Analyze Stepfiles
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
