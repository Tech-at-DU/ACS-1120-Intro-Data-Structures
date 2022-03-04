# Generating Sentences

## Table of Contents <!-- omit in toc -->

1. [Activities](#activities)
1. [Objectives](#objectives)
1. [Challenges](#challenges)
1. [Stretch Challenges](#stretch-challenges)
1. [Resources](#resources)

## Activities

- Compare histogram functions to `Dictogram` and `Listogram` class instance methods
- Discuss advantages of classes and object-oriented programming (OOP)
- Lecture and discussion on building Markov chains and performing random walks

  - Watch [video of lecture on generating sentences with Markov chains]

## Objectives

After completing this class session and the associated tutorial challenges, students will be able to ...

- Build Markov chains based on observed frequency of adjacent words in text
- Generate sentences by sampling words by performing random walks on Markov chain

## Challenges

These challenges are the baseline required to complete the project and course. Be sure to complete these before next class session and before starting on the stretch challenges below.

- [Page 7: Generating Sentences]

  - Build a Markov chain by analyzing frequency of adjacent words in text
  - Sample a random word from a state histogram in a Markov chain
  - Generate a sentence by performing a random walk on Markov chain

## Stretch Challenges

These challenges are more difficult and help you push your skills and understanding to the next level.

- [Page 7: Generating Sentences]

  - Implement `MarkovChain` class to store states of word frequency histograms

    - Add methods for constructing state histograms and sampling words

  - Handle beginning and end of sentences with special start and stop tokens

## Resources

- Read Victor Powell's [visual explanation of Markov chains] and play with the interactive animated diagrams
- Read Alex Dejeu's [article on how Markov chains work][dejeu markov article], with great examples specific to this project (only the "Intro To Markov Models" section; we'll cover the topics in the "Further Markov Model Topics" section later in the course)

[dejeu markov article]: https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
[page 7: generating sentences]: https://bit.ly/tutorial-tweet-generator
[video of lecture on generating sentences with markov chains]: https://www.youtube.com/watch?v=NcmSugXmB-g
[visual explanation of markov chains]: http://setosa.io/blog/2014/07/26/markov-chains/
