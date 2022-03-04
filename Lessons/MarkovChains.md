# Higher Order Markov Chains

## Table of Contents <!-- omit in toc -->

1. [Activities](#activities)
1. [Objectives](#objectives)
1. [Resources](#resources)
1. [Challenges](#challenges)
1. [Stretch Challenges](#stretch-challenges)

## Activities

- Code review implementations of hash table class instance methods
- Lecture and discussion on building higher order Markov chains with larger window sizes

## Objectives

After completing this class session and the associated tutorial challenges, students will be able to ...

- Build higher order Markov chains based on observed frequency of _n_-grams (tuples of _n_ words) in text
- Generate sentences by sampling words by performing random walks on higher order Markov chain
- Utilize a linked list as a queue to track words in a Markov chain's _n_-gram window

## Resources

- Read Victor Powell's [visual explanation of Markov chains] and play with the interactive animated diagrams
- Read Alex Dejeu's [article on how Markov chains work][dejeu markov article], with great examples specific to this project (especially section B, "Further Markov Model Topics" and its subsection 3, "Bigger Windows" on creating higher order Markov chains)
- Read Dataiku's [article on using Markov chains with backoff][dataiku markov article] to generate Donald Trump and Hillary Clinton quotes
- Watch Make School's [Markov chains lecture]
- Review Make School's [Markov chains slides]

## Challenges

These challenges are the baseline required to complete the project and course. Be sure to complete these before next class session and before starting on the stretch challenges below.

- [Page 11: Markov Chains Revisited]

  - Build a second order Markov chain by analyzing frequency of adjacent words in text
  - Sample a random word from a state histogram in second order Markov chain
  - Generate a sentence by performing a random walk on second order Markov chain

- [Page 12: Creating a Corpus][page 11: markov chains revisited]

  - Choose a source with at least 20,000 words (ideally, well over 100,000 words)
  - Collect your corpus (use Diffbot corpus collection script if needed)

## Stretch Challenges

These challenges are more difficult and help you push your skills and understanding to the next level.

- [Page 11: Markov Chains Revisited]

  - Extend code used to build second order Markov chain to build _n_-th order Markov chain for varying values of _n_ (from 1 up to ~5)
  - Implement `MarkovChain` class to store states of word frequency histograms

    - Add methods for constructing state histograms and sampling words

  - Handle beginning and end of sentences with special start and stop tokens

  - Use a linked list as a queue to track words in Markov chain's _n_-gram window
  - Create a deque (double-ended queue) with a doubly-linked list
  - Implement a circular buffer (fixed-size queue) with a fixed-size array

[dataiku markov article]: https://blog.dataiku.com/2016/10/08/machine-learning-markov-chains-generate-clinton-trump-quotes
[dejeu markov article]: https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
[markov chains lecture]: https://www.youtube.com/watch?v=dNaJg-mLobQ
[markov chains slides]: https://github.com/tech-at-du/CS-1.2-Intro-Data-Structures/blob/master/Slides/MarkovChains.pdf
[page 11: markov chains revisited]: https://bit.ly/tutorial-tweet-generator
[page 12: creating a corpus]: https://bit.ly/tutorial-tweet-generator
[visual explanation of markov chains]: http://setosa.io/blog/2014/07/26/markov-chains/
