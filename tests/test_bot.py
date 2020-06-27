# MIT License. This file is part of telegram_me.
#
# Copyright (c) 2020 Hearot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from telegram_me import Link


BOT_BIO = (
    "A @wiki version for wikisource.org. "
    "https://github.com/hearot/wikisourcebot"
)
BOT_IMAGE_CONTENT = "telesco.pe"
BOT_USERNAME = "Wikisource_bot"
BOT_NAME = "Wikisource Search"


def test_bot():
    bot = Link.from_username(BOT_USERNAME)

    assert BOT_BIO == bot.bio
    assert BOT_IMAGE_CONTENT in bot.image
    assert BOT_NAME == bot.name
    assert BOT_USERNAME == bot.username