# @title: count_times_reprinted.R
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description: finds every time the card has been reprinted.

# creates a list of cards that have never been reprinted
setwd("D:/repos/mtg_toolkit/tcgplayer")
tcg <- read.csv("tcg_prices.csv", stringsAsFactors = FALSE)

# group by frequency count
freq_count <- data.frame(table(tcg$card_name))

names(freq_count) <- c("card_name", "reprints")

master <- merge(x = tcg, y = freq_count, by = "card_name", all = TRUE)

write.csv(x = master, file = "tcg_prices.csv", row.names = FALSE)
