<!--
theme: gaia
class: gaia lead
headingDivider: 1
paginate: true
header: Marp CLI Experimental
footer: Transition showcase
backgroundImage: linear-gradient(-20deg, rgba(0, 0, 0, 0.3), transparent)
_paginate: false
_header: ''
_footer: ''

style: |
  @keyframes marp-outgoing-transition-vertical-scroll {
    from { transform: translateY(0%); }
    to { transform: translateY(-100%); }
  }
  @keyframes marp-incoming-transition-vertical-scroll {
    from { transform: translateY(100%); }
    to { transform: translateY(0%); }
  }

  @keyframes marp-outgoing-transition-vflip {
    0% { animation-timing-function: ease-in; }
    50% {
      transform: perspective(100vw) translateZ(-100vw) rotateX(-90deg);
      opacity: 0.5;
      animation-timing-function: step-end;
    }
    100% { opacity: 0; }
  }
  @keyframes marp-incoming-transition-vflip {
    0% {
      animation-timing-function: step-start;
      opacity: 0;
    }
    50% {
      transform: perspective(100vw) translateZ(-100vw) rotateX(90deg);
      opacity: 0.5;
      animation-timing-function: ease-out;
    }
  }

  header, footer { text-align: center; color: currentcolor; }
  section.small-code pre { font-size: 68%; }
-->

# Whatever

**Transition showcase** 🪄


$$\int_0^\infty f(t){dt}$$

# clockwise

<!-- _transition: clockwise -->

```markdown
<!-- transition: clockwise -->
```

# Wipe

<!-- _backgroundColor: #4996C8 -->
<!-- _transition: wipe -->

```markdown
<!-- transition: wipe -->
```

# Aigner
<!-- _transition: wipe -->


![width:400px](./Martin_Aigner.jpg)

- [Proofs from THE BOOK](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK#:~:text=Proofs%20from%20THE%20BOOK%20is,proof%20of%20each%20mathematical%20theorem)
- [Convexity and Aigner's Conjectures](https://arxiv.org/abs/2101.03316)
- Can I prove these with one figure ?


#
<!-- _transition: cube -->
Markov numbers are integers that appear in triples which are solutions of
a Diophantine equation the so-called Markov cubic

$x^2 + y^2 + z^2 - 3x y z = 0.$

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

# 
<!-- _transition: wipe -->
## infinity of Markoff triples: $z=1$

$\begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$
is an automorph of $x^2 + y^2  - 3x y.$

 so $( v_n,v_{n+1},1)$ is a solution where

$\begin{pmatrix}v_{n+1} \\ v_n \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix}1 \\ 1 \end{pmatrix}$

#
### Odd index Fibonacci numbers are Markoff numbers
<!-- _transition: cube -->
$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...$

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

#
<!-- _transition: cube -->
### Frobenius uniqueness conjecture


The largest integer in a triple determines the two other numbers.

#
<!-- _transition: cube -->
### Partial results

m = Markoff number

- Jack Button for [m prime](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610798006292)
- Zhang [An elementary proof...](https://arxiv.org/abs/math/0606283)
- Baragar [m, 3m - 2, 3m + 2 prime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/88B0E426FFCBEA8B3A345C1074B8CC59/S0008439500018828a.pdf/on-the-unicity-conjecture-for-markoff-numbers.pdf)
- [ Bugeaud, Reutenauer, Siksek](https://core.ac.uk/download/pdf/82088222.pdf)
- Conclusion too hard!!!





# coverflow

<!-- _backgroundColor: #ECD03F -->
<!-- _transition: coverflow -->

```markdown
<!-- transition: coverflow -->
```

# cube

<!-- _transition: cube -->

```markdown
<!-- transition: cube -->
```

# cylinder

<!-- _backgroundColor: #EA5555 -->
<!-- _transition: cylinder -->

```markdown
<!-- transition: cylinder -->
```

# diamond

<!-- _backgroundColor: #774ED8 -->
<!-- _transition: diamond -->

```markdown
<!-- transition: diamond -->
```

# drop

<!-- _backgroundColor: #4996C8 -->
<!-- _transition: drop -->

```markdown
<!-- transition: drop -->
```

# explode

<!-- _backgroundColor: #6EB35E -->
<!-- _transition: explode -->

```markdown
<!-- transition: explode -->
```

# fade

<!-- _backgroundColor: #ECD03F -->
<!-- _transition: fade -->

```markdown
<!-- transition: fade -->
```

# fade-out

<!-- _backgroundColor: #F39C3C -->
<!-- _transition: fade-out -->

```markdown
<!-- transition: fade-out -->
```

# fall

<!-- _backgroundColor: #EA5555 -->
<!-- _transition: fall -->

```markdown
<!-- transition: fall -->
```

# flip

<!-- _backgroundColor: #774ED8 -->
<!-- _transition: flip -->

```markdown
<!-- transition: flip -->
```

# glow

<!-- _backgroundColor: #4996C8 -->
<!-- _transition: glow -->

```markdown
<!-- transition: glow -->
```

# implode

<!-- _backgroundColor: #6EB35E -->
<!-- _transition: implode -->

```markdown
<!-- transition: implode -->
```

# in-out

<!-- _backgroundColor: #ECD03F -->
<!-- _transition: in-out -->

```markdown
<!-- transition: in-out -->
```

# iris-in

<!-- _backgroundColor: #F39C3C -->
<!-- _transition: iris-in -->

```markdown
<!-- transition: iris-in -->
```

# iris-out

<!-- _backgroundColor: #EA5555 -->
<!-- _transition: iris-out -->

```markdown
<!-- transition: iris-out -->
```

# melt

<!-- _backgroundColor: #774ED8 -->
<!-- _transition: melt -->

```markdown
<!-- transition: melt -->
```

# overlap

<!-- _backgroundColor: #4996C8 -->
<!-- _transition: overlap -->

```markdown
<!-- transition: overlap -->
```

# pivot

<!-- _backgroundColor: #6EB35E -->
<!-- _transition: pivot -->

```markdown
<!-- transition: pivot -->
```

# pull

<!-- _backgroundColor: #ECD03F -->
<!-- _transition: pull -->

```markdown
<!-- transition: pull -->
```

# push

<!-- _backgroundColor: #F39C3C -->
<!-- _transition: push -->

```markdown
<!-- transition: push -->
```

# reveal

<!-- _backgroundColor: #EA5555 -->
<!-- _transition: reveal -->

```markdown
<!-- transition: reveal -->
```

# rotate

<!-- _backgroundColor: #774ED8 -->
<!-- _transition: rotate -->

```markdown
<!-- transition: rotate -->
```

# slide

<!-- _backgroundColor: #4996C8 -->
<!-- _transition: slide -->

```markdown
<!-- transition: slide -->
```

# star

<!-- _backgroundColor: #6EB35E -->
<!-- _transition: star -->

```markdown
<!-- transition: star -->
```

# swap

<!-- _backgroundColor: #ECD03F -->
<!-- _transition: swap -->

```markdown
<!-- transition: swap -->
```

# swipe

<!-- _backgroundColor: #F39C3C -->
<!-- _transition: swipe -->

```markdown
<!-- transition: swipe -->
```

# swoosh

<!-- _backgroundColor: #EA5555 -->
<!-- _transition: swoosh -->

```markdown
<!-- transition: swoosh -->
```

# wipe

<!-- _backgroundColor: #774ED8 -->
<!-- _transition: wipe -->

```markdown
<!-- transition: wipe -->
```

# wiper

<!-- _backgroundColor: #4996C8 -->
<!-- _transition: wiper -->

```markdown
<!-- transition: wiper -->
```

# zoom

<!-- _backgroundColor: #6EB35E -->
<!-- _transition: zoom -->

```markdown
<!-- transition: zoom -->
```

# And more, make your own!

<!-- _class: lead invert -->
<!-- _transition: vertical-scroll -->
<!-- _footer: '**Example**: vertical-scroll' -->

<!-- prettier-ignore-start -->

```css
@keyframes marp-outgoing-transition-vertical-scroll {
  from { transform: translateY(0%); }
  to { transform: translateY(-100%); }
}

@keyframes marp-incoming-transition-vertical-scroll {
  from { transform: translateY(100%); }
  to { transform: translateY(0%); }
}
```

<!-- prettier-ignore-end -->

# Try making more creative transitions!

<!-- _class: lead invert small-code -->
<!-- _backgroundColor: #0bf -->
<!-- _transition: vflip 1s -->
<!-- _footer: '**Example**: vflip' -->

<!-- prettier-ignore-start -->

```css
@keyframes marp-outgoing-transition-vflip {
  0% { animation-timing-function: ease-in; }
  50% {
    transform: perspective(100vw) translateZ(-100vw) rotateX(-90deg);
    opacity: 0.5;
    animation-timing-function: step-end;
  }
  100% { opacity: 0; }
}
@keyframes marp-incoming-transition-vflip {
  0% {
    animation-timing-function: step-start;
    opacity: 0;
  }
  50% {
    transform: perspective(100vw) translateZ(-100vw) rotateX(90deg);
    opacity: 0.5;
    animation-timing-function: ease-out;
  }
}
```

<!-- prettier-ignore-end -->

# Marp CLI experimental

**Transition showcase** 🪄

https://github.com/marp-team/marp-cli/issues/447

<!-- header: "" -->
<!-- footer: "" -->
<!-- paginate: false -->
<!-- _transition: fade -->

---

<!-- _class: invert lead -->

Marp CLI's preview mode `--preview` can try transitions easily!

```bash
marp --template bespoke --bespoke.transition --preview ./transition.md
```

Experimental transition is depending on [Shared Element Transitions proposal](https://github.com/WICG/shared-element-transitions), and available in Marp CLI v2.0.0 and later + Chrome/Chromium 101 and later w/ "documentTransition API" experiment.
