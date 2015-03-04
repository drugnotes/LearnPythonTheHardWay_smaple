#!/usr/bin/python
# -*- coding: utf-8 -*-

# 定义一个格式字符串变量formatter
formatter = "%r %r %r %r"

# 打印输出不同格式的formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)