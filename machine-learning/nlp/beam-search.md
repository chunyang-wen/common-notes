### Beam search

`Beam search` normally is used in NLP (Sequence2Sequence model). When we predict the output, we
get the output with the highest probability. It is called beam search with size = 1.

We assume the beam search size is equal to N. Then at each step, we get the top N highest output
according to their probabilities.

A detailed example:

```python
vocab = [a, b, c]
beam_size = 2

# step 1 from (a, b, c)
output_1 = [a, c]

# step2 from (aa, ab, ac, ca, cb, cc)
output_2 [ac, cc]
```

Select the top N.
