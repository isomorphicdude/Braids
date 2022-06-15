# Braids

## 0 Introduction  

This is an attempt to implement braid groups in python with implementation of *Dehornoy's algorithm* and *Garside normal form* (improved by Morton et al.).  

Braids are geometric objects with rich algebraic and topological properties. One classical representation is given by Artin.  

$$
\begin{equation}
    B_n= \langle{ \sigma_1, \cdots, \sigma_{n-1}| \begin{cases}
    \sigma_i\sigma_j = \sigma_i\sigma_j & \lvert i-j \rvert>1 \\ 
    \sigma_i\sigma_j\sigma_i = \sigma_j\sigma_i \sigma_j & \lvert i-j \rvert=1 
    \end{cases}} \rangle
\end{equation} 
$$  

## 1 The Word Problem  

A word $\omega$ is $\sigma_1^{e_1}\cdots\sigma_n^{e_n}$, expressed in the generators, where $e_i \in \{1, -1\}$.  

For any $\omega, \omega' \in B_n$, we are interested in whether there exists an algorithm determining their equivalence, that is, if there is way to apply fundamental relations described in (1) and basic group operations $\sigma_i \sigma_i^{-1}=\sigma_i^{-1}\sigma_i=1$ to transform one word to another. This is also the algebraic version of braids isoptopy problem.  

## 1.1 Dehornoy's Algorithm  

Dehornoy showed that $B_n$ is left oderable, *i.e.* $a<b \implies ca<cb, \forall a,b \in B_n$; this is equivalent to the group $B_n$ having the structure $B_n=P\cup \{1\}\cup P^{-1}$, where $P:=\{a \in B_n: \ 1<a\}$ and $P^{-1}:=\{b \in B_n: \ b<1\}$.  

He defined a *reduced braid* as those with *main generators* ($\sigma_i$ with the smallest index) having only positive/negative exponents.   

It was also shown that $P$ above coincides with the set of words in which the $\sigma_i$ of the smallest index only occurs positively, that is *positively reduced*.  

To solve the word problem, Dehornoy noted that every braid admits a *reduced* form and it's only $1$ when the *reduced* form is trivial. He then observed that a braid being *reduced* is equivalent to containing no *handles*.  

Thus, to determine if two braids $\omega, \omega'$ are equal, we can remove all the handles in $\omega \omega'$ and compare it with the trivial braid.   

A $\sigma_j-$ *handle* is a word of the form $\sigma_j^e v \sigma_j^{-e}$, $v$ does not contain $\sigma_j$. A *main handle* is defined similarly for minimal $j$.  

Note that if a $\sigma_j$-handle does not contain a $\sigma_{j+1}$-handle then the word is *permitted*(we can proceed).   

### Algorithm  

- Find the leftmost permitted $\sigma_j^{-e} v \sigma_j^e$
- Apply transformation by 
  - $\sigma_{j}^{\pm 1} \mapsto 1$
  -  $\sigma_{j+1}^{\pm 1} \mapsto \sigma_{j+1}^{-e}\sigma_j^{\pm 1} \sigma_{j+1}^{e}$
  -  identity for other generators
-  Repeat above two steps

Remark: this algorithm is $\mathcal{O}(\exp(|\omega|))$.   


## 1.2 Garside's Normal Form (improved)  

This gives an algorithm that is approximately $\mathcal{O}(|\omega|^2)$  

We define the fundamental braid as $\Delta:=(\sigma_1 \cdots \sigma_{n-1})(\sigma_1 \cdots \sigma_{n-2})\cdots(\sigma_1)$; note in some literature, this is defined as $\Delta = (\sigma_{n-1} \cdots \sigma_1)(\sigma_{n-1} \cdots \sigma_2)\cdots(\sigma_{n-1})$, those are the same as $\sigma_i \Delta = \Delta \sigma_{n-i}$.  

### Algorithm:  

- Eliminate all generators with negative exponents in the word $\omega$ by applying $\sigma_i^{-1}=\Delta^{-1} \sigma_i^*$  
  
- Move all $\Delta$ to the left end and obtain the form $\omega=\Delta^r \omega'=\Delta^r B_1 \cdots B_n$, $B_i \in S_n^+$  

- Check if for each $i$, we have $S(B_{i+1})\subset F(B_i)$  
- If so, then this admits a *left-weighted factorisation*, which is unique  
- Else, find first $i$, s.t. $S(B_{i+1})\nsubseteq F(B_i)$, replace with $C_{i}=B_i\sigma_j, C_{i+1}=\sigma_j^{-1}B_{i+1}$, for $j \in S(B_{i+1})$, repeat for all such $j$; note this process eventually terminates as for a fixed total weight.  
- Repeat the three steps above.  

### Implementation Details:  

- We note that $\pi(i+1) < \pi(i)$ for the permutation braid $A_{\pi}$ is equivalent to $i \in S(A_{\pi})$  

- So it is useful to compute beforehand the corresponding permutations for each braid and note if $\pi(i+1) < \pi(i)$  

- To check if $i \in F(A_{\pi})$, we simply note that $F(A_{\pi})=S({\rm rev} A_{\pi})$, so we repeat the steps above

## 2 The Conjugacy Problem   

We are also interested in determining whether two words are in the same conjugacy class.  

We write the conjugacy class for a word $\omega$ as $[\omega]$. 

## 2.1 The Super Summit Set  

We define the *super summit set* of a word $\omega$ as the subset with maximal $\inf$ and minimal $\sup$ w.r.t the partial ordering introduced by Morton et al. This subset is unique w.r.t. the conjugacy class of a braid, thus we can compute this set given two words.   

We remark here that the algorithm is $\mathcal{O}(\exp(|\omega|))$.  

## 2.2 Application  in Cryptography  

We note an application of the conjugacy algorithm being exponential.  



## 3.0 Non-minimal Braid (for interest)  

Given a word $\omega$ in the generators $\sigma_1, \cdots , \sigma_{n-1}$,  we would like to know if there exists a word $\omega'$ with shorter length in the same generators, which represents the same word.   

A brute-force search listing all possible shorter words can be used for verification.  

In 1991 Patterson and Razborov proved that this problem is $NP-$*complete*, which means if we were able to find an algorithm of $\mathcal{O}(p(|\omega|))$, then we would have shown $P=NP$.  

## To Do:  

- [x] `braid` class implementation  
- [ ] `dehornoy`  implementation
- [ ] `garside`  implementation  
- [x] `garside` implementation details  
- [ ] `isconjugate` method implementation 
- [ ] Experimenting
- [ ] Analysis of word problem algorithms
