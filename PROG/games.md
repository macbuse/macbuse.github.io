# Games


La théorie des jeux est un domaine des mathématiques qui s'intéresse aux interactions stratégiques des agents (appelés « joueurs »). Les fondements mathématiques de la théorie moderne des jeux sont décrits autour des années 1920 par Ernst Zermelo dans l'article Über eine Anwendung der Mengenlehre auf die Theorie des Schachspiels, et par Émile Borel dans l'article « La théorie du jeu et les équations intégrales à noyau symétrique ». Ces idées sont ensuite développées par Oskar Morgenstern et John von Neumann en 1944 dans leur ouvrage Theory of Games and Economic Behavior qui est considéré comme le fondement de la théorie des jeux moderne. Il s'agissait de modéliser les jeux à somme nulle où la somme des gains entre les joueurs est toujours égale à zéro. La théorie des jeux devient dès ce moment un outil théorique important de la microéconomie.

## Equilibre de Nash

Dans sa thèse, Nash présente une situation d’équilibre qui deviendra bientôt l’« équilibre de Nash ». Par équilibre, il entend une situation dans laquelle aucun des joueurs ne peut trouver de meilleure stratégie de jeu, compte tenu des stratégies choisies par les autres joueurs.


## dilemme du prisonnier

- [dilemme du prisonnier](https://fr.wikipedia.org/wiki/Dilemme_du_prisonnier)


Tucker suppose deux prisonniers (complices d'un crime) retenus dans des cellules séparées et qui ne peuvent pas communiquer ; l'autorité pénitentiaire offre à chacun des prisonniers les choix suivants :

- si un seul des deux prisonniers dénonce l'autre, il est remis en liberté alors que le second obtient la peine maximale (10 ans) ;
- si les deux se dénoncent entre eux, ils seront condamnés à une peine plus légère (5 ans) ;
- si les deux refusent de dénoncer, la peine sera minimale (6 mois), faute d'éléments au dossier.

Ce problème modélise bien les questions de politique tarifaire : le concurrent qui baisse ses prix gagne des parts de marché et peut ainsi augmenter ses ventes et accroître éventuellement son bénéfice, mais si son concurrent principal en fait autant, les deux peuvent y perdre.

Ce jeu ne conduit pas spontanément à un état où on ne pourrait améliorer le bien-être d'un joueur sans détériorer celui d'un autre (c'est-à-dire un optimum de Pareto ; voir aussi équilibre de Nash). À l'équilibre, chacun des prisonniers choisira probablement de faire défaut alors qu'ils gagneraient à coopérer : chacun est fortement incité à tricher, ce qui constitue le cœur du dilemme.

Si le jeu était répété, chaque joueur pourrait user de représailles envers l'autre joueur pour son absence de coopération, ou même simplement minimiser sa perte maximale en trahissant les fois suivantes. L'incitation à tricher devient alors inférieure à la menace de punition, ce qui introduit la possibilité de coopérer : la fin ne justifie plus les moyens.


## Paradoxe de Braess

En mathématiques, et plus précisément en théorie des jeux, le paradoxe de Braess énonce que l'ajout d'une nouvelle route dans un réseau routier peut réduire la performance globale, lorsque les entités se déplaçant choisissent leur route individuellement. Cela provient du fait que l'équilibre de Nash d'un tel système n'est pas nécessairement optimal. Ce paradoxe a été mis en évidence en 1968 par le mathématicien Dietrich Braess1.

[math en jean](http://www.mathenjeans.fr/sites/default/files/comptes-rendus/2015-braess-cluj_briancon.pdf)

## GANs

GANs are a competing game between two neural networks trained in an adversarial manner to reach a Nash equilibrium. ... This paper reviews literature that leverages the game theory in GANs and addresses how game models can relieve specific generative models' challenges and improve the GAN's performance.


[Style Transfer](https://towardsdatascience.com/style-transfer-with-gans-on-hd-images-88e8efcf3716)


## Price of anarchy

The Price of Anarchy (PoA) [1] is a concept in economics and game theory that measures how the efficiency of a system degrades due to selfish behavior of its agents in the worst case. It is a general notion that can be extended to diverse systems and notions of efficiency. For example, consider the system of transportation of a city and many agents trying to go from some initial location to a destination. Let efficiency in this case mean the average time for an agent to reach the destination. In the 'centralized' solution, a central authority can tell each agent which path to take in order to minimize the average travel time. In the 'decentralized' version, each agent chooses its own path. The Price of Anarchy measures the ratio between average travel time in the two cases.

Usually the system is modeled as a game and the efficiency is some function of the outcomes (e.g. maximum delay in a network, congestion in a transportation system, social welfare in an auction, ...). Different concepts of equilibrium can be used to model the selfish behavior of the agents, among which the most common is the Nash equilibrium. Different flavors of Nash equilibrium lead to variations of the notion of Price of Anarchy as Pure Price of Anarchy (for deterministic equilibria), Mixed Price of Anarchy (for randomized equilibria), and Bayes–Nash Price of Anarchy (for games with incomplete information). Solution concepts other than Nash equilibrium lead to variations such as the Price of Sinking.[2]

The term Price of Anarchy was first used by Elias Koutsoupias and Christos Papadimitriou, but the idea of measuring inefficiency of equilibrium is older.[3] The concept in its current form was designed to be the analogue of the 'approximation ratio' in an approximation algorithm or the 'competitive ratio' in an online algorithm. This is in the context of the current trend of analyzing games using algorithmic lenses (algorithmic game theory).


## Deepmind

[wiki](https://en.wikipedia.org/wiki/DeepMind)

- [alphago](https://en.wikipedia.org/wiki/AlphaGo)
- [alphazero](https://en.wikipedia.org/wiki/AlphaZero)
- [vs stockfish](https://www.chess.com/news/view/updated-alphazero-crushes-stockfish-in-new-1-000-game-match)

### D3C

Even in simple multi-agent systems, fixed incentives can lead to outcomes that are poor for the group and each individual agent. We propose a method, D3C, for online adjustment of agent incentives that reduces the loss incurred at a Nash equilibrium. Agents adjust their incentives by learning to mix their incentive with that of other agents, until a compromise is reached in a distributed fashion. We show that D3C improves outcomes for each agent and the group as a whole on several social dilemmas including a traffic network with Braess's paradox, a prisoner's dilemma, and several reinforcement learning domains.


[Source](https://deepmind.com/research/publications/2020/D3C-Reducing-the-Price-of-Anarchy-in-Multi-Agent-Learning)

<script src="https://gist.github.com/bucketh3ad/11362275.js"></script>`
