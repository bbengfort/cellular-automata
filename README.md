# Cellular Automata [![Build Status][travis_img]][travis_url] #
Animated Cellular Automata using Matplotlib

[Cellular automata][cellular_automaton] are models of dynamical systems in discrete time, space, and state inspired by the work of [Jon von Neumann][vonneumann] in the 1950s. He conceived of a world of machines (cells) inhabiting a chessboard space, but instead of simply being black or red, the machine's state was identified by its color. These models are used often in [Artificial Life][artificial_life] Simulations as well as parallel computational devices because the illustrate the following fundamentals of natural computing:

* explicit space and time
* [locality for massive parallelism][massive_parallel]
* [self-organization][self_organization]
* [emergent properties][emergence]
* lifelike behavior

For my part- they are extremely cool, and programming them is extremely fun. Although there are many tools and animations for building visual Cellular Automata, I found very little in the way of Python libraries. This library uses [matplotlib 1.3.1][matplotlib] to animate the behavior of cellular automata, and allows a researcher to use Python to build and visualize these very cool looking machines!

## Dependencies ##
This library depends on Python data libraries, particularly matplotlib and numpy. These libraries have a lot of compiling under the hood; you need to ensure that you have a Fortran compiler, and that you have ffmpeg libraries installed. Installing on a Mac (which this was developed on) is also notoriously difficult, so there are some Mac-specific hacks in the code. If you're getting errors trying to get the program to run, don't fear; it might not be the code, just the coder! Feel free to leave an issue and we'll sort it out together.

<!-- References -->
[travis_img]: https://travis-ci.org/bbengfort/cellular-automata.png?branch=master
[travis_url]: https://travis-ci.org/bbengfort/cellular-automata
[cellular_automaton]: http://mathworld.wolfram.com/CellularAutomaton.html
[vonneumann]: http://ei.cs.vt.edu/~history/VonNeumann.html
[artificial_life]: http://en.wikipedia.org/wiki/Artificial_life
[massive_parallel]: http://en.wikipedia.org/wiki/Massively_parallel_(computing)
[self_organization]: http://en.wikipedia.org/wiki/Self-organization
[emergence]: http://en.wikipedia.org/wiki/Emergent_properties#Emergent_properties_and_processes
[matplotlib]: http://matplotlib.org/
