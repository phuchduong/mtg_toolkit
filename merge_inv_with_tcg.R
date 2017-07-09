# @title: merge_inv_with_tcg.py
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description: merge inventory sheet with tcgplayer price list

setwd("D:/repos/mtg_toolkit")
inv = read.csv("inventory.csv", stringsAsFactors = FALSE)
tcg = read.csv("tcgplayer/tcg_prices.csv", stringsAsFactors = FALSE)

