# Text-Generator-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/134

## Work on project. Stage 2/6: Break the dataset into bigrams
### Objectives

In order to prepare the corpus for use in this project, we need to take the following important steps:

1. Transform the corpus into a collection of bigrams. The results should contain all the possible bigrams from the corpus, which means that:
— Every token from the corpus should be a head of a bigram with the exception of the last token which cannot become a head since nothing follows it;
— Every token from the corpus should be a tail of a bigram with the exception of the first token which cannot possibly be the tail of a bigram because nothing precedes it.
2. Take an integer as user input and print the bigrams with the corresponding index. Repeat this process until the string ```exit``` is input. Also, make sure that
the input is actually an integer that falls in the range of the collection of bigrams. If that is not the case, print an error message and request a new input. 
Error messages should contain the types of errors (```Type Error```, ```Value Error```, ```Index Error```, etc.). Each bigram should have
the format ```Head: [head] Tail: [tail]``` and should be printed in a new line.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

The output of the program should look like this. Note that this is just an example: you might get completely different results.

```shell
> corpus.txt
Number of bigrams: 2343554

> 0
Head: What     Tail: do
> 4
Head: They're  Tail: savages.
> 5
Head: savages. Tail: One
> 34
Head: I've     Tail: never
> 42
Head: ever     Tail: in
> 256
Head: the      Tail: lads
> 453
Head: sentence Tail: you
> 2345
Head: don't    Tail: understand
> 3000
Head: can      Tail: protect
> 943287563823572346
Index Error. Please input a value that is not greater than the number of all bigrams.
> six
Type Error. Please input an integer.
> -1
Head: the      Tail: North!
> exit
```
