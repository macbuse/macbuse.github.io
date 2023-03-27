# -*- coding: utf-8 -*-

#IMPORTANT: if you add a template to this file please make it *raw utf8*
#by adding the letters ur before the string

#I had to split the TeX header from the rest and write it as ascii

committee = {"PRESIDENT" : "Erwan Lanneau",
"VOTANTS" : 14,
"NULS" : 0,
"OUI" : 14,
"NON" : 0,
"SCALE" : .2,
"DATE" : "now"
}



motifs = {'demission': '''le candidat a retir\'e sa candidature.''',
          'a' : r'''Compte tenu du sujet de recherche du candidat
          une int\'egration au sein du laboratoire est difficilement envisageable.''',
'ab': r'''Compte tenu du sujet de recherche du candidat,
          une int\'egration au sein du laboratoire est difficilement envisageable.''',
'b': r'''Le  dossier du candidat  pr\'esente un projet de rechereche int\'eressant
par rapport aux th\'ematiques du laboratoire mais le comit\'e juge prudent d'attendre un an ou plus  pour suivre son \'evolution.
''',
'c': r'''Le  niveau du concours \'etant tr\`es \'elev\'e cette ann\'ee
la qualit\'e du dossier  n'est pas suffisante pour demander l'audition du candidat. 
''',
'ac': r'''Compte tenu du sujet de recherche du candidat, une int\'egration au sein
du laboratoire est difficilement envisageable. Le  niveau du concours \'etant tr\`es \'elev\'e,
le comit\'e ne demande pas l'audition du candidat.''',
'bc': r'''Le  dossier du candidat  pr\'esente un projet de rechereche int\'eressant par rapport aux th\'ematiques du laboratoire mais le comit\'e juge prudent d'attendre un an ou plus
pour suivre son \'evolution. Le  niveau du concours \'etant tr\`es \'elev\'e, le comit\'e ne demande pas l'audition du candidat.'''
}




header = r'''\documentclass[a4paper, 12pt, titlepage]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage{{amsmath,amssymb}}
\usepackage[french]{{babel}}
\selectlanguage{{french}}
\usepackage{{enumerate}}
\usepackage{{graphicx}}


\newcommand{{\R}}{{\mathbb{{R}}}}
\newcommand{{\C}}{{\mathbb{{C}}}}
\def\no{{\noindent}}
\def\vs{{\vskip 1cm}}
\def\ben{{\begin{{enumerate}}}}
\def\een{{\end{{enumerate}}}}

\begin{{document}}
\pagestyle{{empty}}
'''


texTemplateProf = r'''

\begin{{center}}
{{\Large {Corps} {N° emploi}: Rapport sur la candidature de }}
\end{{center}}
\vs

\no
{{\bf {{\large Nom}} :}} {Nom}\\
{{\bf Prénom :}} {Prénom}\\
{{\bf Date de naissance :}} {Né(e) le}\\
{{\bf Fonction actuelle :}} {Situation professionnelle},\\ {Lieu d'exercice} \\


\vs
\no
{{\bf {{\large HDR}} :}} {Titre thèse}\\
{{\bf Date :}} {Date soutenance}\\
{{\bf Etablissement :}} {Lieu soutenance}\\
{{\bf Directeur :}} {Directeur Thèse}\\
{{\bf Jury :}} {Jury}\\
\\
\no
{{\bf Mots cl\'es :}}\\


\section*{{Publications}}


\ben
\item \`a remplir
\een

{{\textbf{{  Informations fournies : }} {Travaux}


\section*{{Enseignement}}

\ben
\item \`a remplir
\een

{{\textbf{{  Informations fournies : }}{Activités enseignement}


\section*{{Encadrement}}


\ben
\item \`a remplir
\een

\section*{{Administration}}

\ben
\item \`a remplir
\een

{{\textbf{{  Informations fournies : }}{Activités administratives}



\section*{{Rayonnement}}
\ben
\item \`a remplir
\een


\section*{{Rapport scientifique}}

\subsection*{{Domaine de recherche}}

{Activités recherche}

\subsection*{{Conclusion}}




\vs
\no
Date et signature :




\end{{document}}
'''

texTemplateProf2 = r'''

\begin{{center}}
{{\Large {Corps} {N° emploi:.0f}-{Numéro Gesup}: Rapport sur la candidature de }}
\end{{center}}
\vs

\no
{{\bf {{\large Nom}} :}} {Nom}\\
{{\bf Prénom :}} {Prénom}\\
{{\bf Date de naissance :}} {Né(e) le}\\
{{\bf Fonction actuelle :}} {Situation professionnelle},\\ {Lieu d'exercice} \\


\vs
\no
{{\bf {{\large HDR}} :}} {Titre thèse}\\
{{\bf Date :}} {Date soutenance}\\
{{\bf Etablissement :}} {Lieu soutenance}\\
{{\bf Directeur :}} {Directeur Thèse}\\
{{\bf Jury :}} {Jury}\\
\\
\no
{{\bf Mots cl\'es :}}\\


\section*{{Publications}}


{{\textbf{{  Informations fournies : }} {Travaux}


\section*{{Enseignement}}


{{\textbf{{  Informations fournies : }}{Activités enseignement}


\section*{{Encadrement}}


\section*{{Administration}}


{{\textbf{{  Informations fournies : }}{Activités administratives}



\section*{{Rayonnement}}


\section*{{Rapport scientifique}}

\subsection*{{Domaine de recherche}}

{Activités recherche}

\subsection*{{Conclusion}}




\vs
\no
Date et signature :




\end{{document}}
'''

texTemplateMCF = r'''

\begin{{center}}
{{\Large {Corps} {N° emploi:.0f}-{Numéro Gesup}: Rapport sur la candidature de }}
\end{{center}}
\vs

\no
{{\bf {{\large Nom}} :}} {Nom}\\
{{\bf Prénom :}} {Prénom}\\
{{\bf Date de naissance :}} {Né(e) le}\\
{{\bf Fonction actuelle :}} {Situation professionnelle},\\ {Lieu d'exercice} \\


\vs
\no
{{\bf {{\large Thèse}} :}} {Titre thèse}\\
{{\bf Date :}} {Date soutenance}\\
{{\bf Etablissement :}} {Lieu soutenance}\\
{{\bf Directeur :}} {Directeur Thèse}\\
{{\bf Jury :}} {Jury}\\
\\
\no
{{\bf Mots clés :}}\\
{{\bf Avis sur l'audition du candidat :}} d\'efavorable/possible/tr\`es favorable \\

\section{{Publications}}


\ben
\item \`a remplir
\een

{{\textbf{{  Informations fournies :}} {Travaux}


\section{{Activités enseignement}}

\ben
\item \`a remplir
\een

{{\textbf{{  Informations fournies :}}{Activités enseignement}


\section{{Administration}}

\ben
\item \`a remplir
\een

{{\textbf{{  Informations fournies :}}{Activités administratives}



\section{{Autres (encadrement, animation, contrats, prix)}}
\ben
\item \`a remplir
\een


\section{{Rapport scientifique}}

\section*{{Domaine de recherche}}

{Activités recherche}

\section*{{Avis sur le dossier}}

\textit{{Texte de synthèse du rapporteur}}

\vs
\no
Date et signature :

\end{{document}}
'''



texTemplateAudition = r'''
\begin{{center}}
{{\Large {Corps} {N° emploi:.0f}-{Numéro Gesup}: Rapport sur l'audition de }}
\end{{center}}
\vs

\no
{{\bf {{\large Nom}} :}} {Nom}\\
{{\bf Prénom :}} {Prénom}\\
{{\bf Date de naissance :}} {Né(e) le}\\


{Nom} a confirm\'e l'evaluation des rapporteurs.
Il a commenc\'e par presenter son  parcours de formation.

Par la suite {Prénom} a abord\'e
son activit\'e de recherche sur {Activités recherche}
{Nom}  a expliqu\'e ses r\'esultats
avec
clart\'e,
faisant preuve de dynamisme dans sa recherche.
Nous etions
satisfaits
\'epat\'es
par son exposition.

Quant \`a la question d'int\'egration au laboratoire,
{Prénom} nous a signal\'e que l'\'equipe de
topologie
algebre et g\'eom\'etrie
physique math\'ematique
th\'eorie de nombres
analyse et g\'eom\'etrie
est le plus proche \`a ses inter\^ts.
En particulier {Nom} envisage de travailler avec
...


Sa maitrise du francaise
est adequate/excellente.
Nous avons pu constater que {Nom} ,
par sa presentation et sa facon de d'expliquer
ses r\'esultats,
est tout \`a fait  pr\^et \`a
assurer les cours d\`es la rentr\'ee 2013.



\vs
\begin{{flushright}}Fait \`a St. Martin d'H\`eres

\includegraphics[scale=.8]{{mysig.jpg}}
\end{{flushright}}

'''

Audition = r'''
\begin{{center}}
{{\Large
UNIVERSITE GRENOBLE ALPES\\
AVIS DU COMITE DE SELECTION\\
}}
\end{{center}}
Postes {Corps} {N° emploi:.0f} \\
Laboratoire : IF Unité 5582\\


\vs

\no
\textbf{{\large Candidat :}}
{{\bf {{Nom}} :}} {Nom}
{{\bf Prénom :}} {Prénom}\\
{{\bf Date de naissance :}} {Né(e) le}\\

\begin{{center}}
\textbf{{Délibération du comité de sélection}}
\end{{center}}

\no
Après examen du dossier de candidature
qui s’est déroulée le {DATE}
les membres du comité de sélection ont émis
un avis favorable sur votre candidature.

\vs\no
\textbf{{D\'etail du vote}}\\
Votants : {VOTANTS}\\
Nuls : $(NULS)s \\
\no
\textbf{{Suffrages exprim\'es}}\\
OUI : {OUI}\\
NON ou BLANCS : {NON}
\vs
\no
Signature du président du comité de sélection

\begin{{flushright}}Fait \`a St. Martin d'H\`eres

\includegraphics[scale=.8]{{mysig.jpg}}
{PRESIDENT}
\end{{flushright}}



\textbf{{ Avis motivé du comité de sélection sur la candidature}}
\no

Excellent dossier. Int\'egration au labo sans probl\`eme.

'''

nonAudition = r'''
\begin{{center}}
{{\Large
UNIVERSITE GRENOBLE ALPES\\
AVIS DU COMITE DE SELECTION\\
}}
\end{{center}}
Poste : {Corps} {N° emploi:.0f}\\
Laboratoire : IF Unit\'e 5582\\


\vs

\no
\textbf{{ Candidat :}}
{{{{Nom}} :}} {Nom}
{{Pr\'enom :}} {Prénom}\\
{{Date de naissance :}} {Né(e) le}\\

\begin{{center}}
\textbf{{D\'elib\'eration du comit\'e de s\'election}}
\end{{center}}

\no
Apr\`es examen du dossier de candidature
qui s’est d\'eroul\'ee le {DATE}
les membres du comité de sélection ont \'emis
un avis défavorable sur votre candidature.

\vs\no
\textbf{{D\'etail du vote}}\\
Votants : {VOTANTS}\\
Nuls : {NULS} \\
\no
\textbf{{Suffrages exprim\'es}}\\
OUI : {OUI}\\
NON ou BLANCS : {NON}
\vs
\no
Signature du président du comité de sélection

\begin{{flushright}} Fait \`a St. Martin d'H\`eres

\includegraphics[scale={SCALE}]{{mysig.jpg}}
{PRESIDENT}


\end{{flushright}}



\begin{{center}}
\textbf{{ Avis motiv\'e du comit\'e de s\'election sur la candidature}}
\end{{center}}

\no
'''

#Fait \`a St. Martin d'H\`eres
