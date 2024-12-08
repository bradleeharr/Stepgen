# Stepgen
Autostepper


# Inspiration:
https://github.com/chrisdonahue/ddc

https://github.com/phr00t/AutoStepper

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


### NN-Based
* - [ ] Gather Stepfiles
  - [ ] Create DNN
  - [ ] Test first approach
 
* - [ ] Review [DanceDanceConvolution](https://github.com/chrisdonahue/ddc)
