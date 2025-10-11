# sleep = read.csv("sleep.csv", colClasses=c("factor", "numeric"))
noscreen = read.csv("nosleep.csv")$Sleep
mean(noscreen)
n_noscreen = 35
highscreen = read.csv("highscreen.csv")$Sleep
mean(highscreen)
n_highscreen = 40

S2p = ((n_noscreen - 1) * var(noscreen)**2 + (n_highscreen - 1) * var(highscreen)**2 ) / (n_noscreen + n_highscreen - 2)
Sp = sqrt(S2p)

z = (mean(noscreen)-mean(highscreen)) / (Sp * sqrt(1/n_noscreen + 1/n_highscreen))
