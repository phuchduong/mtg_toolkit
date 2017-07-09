# @title: check_for_spell_mistakes.R
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description:  cross references inventory card name with tcgplayer card
#               names to find spelling mistakes.

setwd("D:/repos/mtg_toolkit")
inv = read.csv("inventory.csv", stringsAsFactors = FALSE)
tcg = read.csv("tcgplayer/tcg_prices.csv", stringsAsFactors = FALSE)
