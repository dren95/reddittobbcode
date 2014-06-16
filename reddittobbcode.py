import sys
import time
import socket
import re
import argparse
import HTMLParser

import praw
import requests
 
def markdown_to_bbcode(s):
    links = {}
    codes = []
    def gather_link(m):
        links[m.group(1)]=m.group(2); return ""
    def replace_link(m):
        return "[url=%s]%s[/url]" % (links[m.group(2) or m.group(1)], m.group(1))
    def gather_code(m):
        codes.append(m.group(3)); return "[code=%d]" % len(codes)
    def replace_code(m):
        return "%s" % codes[int(m.group(1)) - 1]
    
    def translate(p="%s", g=1):
        def inline(m):
            s = m.group(g)
            s = re.sub(r"(`+)(\s*)(.*?)\2\1", gather_code, s)
            s = re.sub(r"\[(.*?)\]\[(.*?)\]", replace_link, s)
            s = re.sub(r"\[(.*?)\]\((.*?)\)", "[url=\\2]\\1[/url]", s)
            s = re.sub(r"<(https?:\S+)>", "[url=\\1]\\1[/url]", s)
            s = re.sub(r"\B([*_]{2})\b(.+?)\1\B", "[b]\\2[/b]", s)
            s = re.sub(r"\B([*_])\b(.+?)\1\B", "[i]\\2[/i]", s)
            return p % s
        return inline
    
    s = re.sub(r"(?m)^\[(.*?)]:\s*(\S+).*$", gather_link, s)
    s = re.sub(r"(?m)^    (.*)$", "~[code]\\1[/code]", s)
    s = re.sub(r"(?m)^(\S.*)\n=+\s*$", translate("~[size=200][b]%s[/b][/size]"), s)
    s = re.sub(r"(?m)^(\S.*)\n-+\s*$", translate("~[size=100][b]%s[/b][/size]"), s)
    s = re.sub(r"(?m)^#\s+(.*?)\s*#*$", translate("~[size=200][b]%s[/b][/size]"), s)
    s = re.sub(r"(?m)^##\s+(.*?)\s*#*$", translate("~[size=100][b]%s[/b][/size]"), s)
    s = re.sub(r"(?m)^###\s+(.*?)\s*#*$", translate("~[b]%s[/b]"), s)
    s = re.sub(r"(?m)^> (.*)$", translate("~[quote]%s[/quote]"), s)
    s = re.sub(r"(?m)^[-+*]\s+(.*)$", translate("~[list]\n[*]%s\n[/list]"), s)
    s = re.sub(r"(?m)^\d+\.\s+(.*)$", translate("~[list=1]\n[*]%s\n[/list]"), s)
    s = re.sub(r"(?m)^((?!~).*)$", translate(), s)
    s = re.sub(r"(?m)^~\[", "[", s)
    s = re.sub(r"\[/code]\n\[code(=.*?)?]", "\n", s)
    s = re.sub(r"\[/quote]\n\[quote]", "\n", s)
    s = re.sub(r"\[/list]\n\[list(=1)?]\n", "", s)
    s = re.sub(r"(?m)\[code=(\d+)]", replace_code, s)
    
    return s

def main():
    parser = argparse.ArgumentParser(
        description='Prep reddit submission w/ comments for posting on bbcode forum. Comment hierarchy is preserved and markdown syntax is converted to bbcode where possible.'
    )
    parser.add_argument('submission_id', help='reddit base 36 submission id')
    parser.add_argument('-s', dest='spaces', action='store_true',
                        help='spaces instead of &nbsp;')

    args = parser.parse_args()

    r = praw.Reddit("reddittobbcode/1.0 by dren")

    submission = None
    while submission is None :
        try:
            submission = r.get_submission(submission_id=args.submission_id, comment_limit=None)
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, socket.error, socket.timeout) as e:
            print >> sys.stderr, 'NETWORK ERROR: retrying in 1s...'
            time.sleep(1)
            continue

    html = HTMLParser.HTMLParser()

    print '[url=%s]%s[/url]' % (submission.permalink, submission.title)
    print 'submitted by %s' % (submission.author.name if submission.author is not None else '[deleted]', )
    print 
    print html.unescape(markdown_to_bbcode(submission.selftext))
    print 

    comment_stack = [iter(submission.comments)]
    while len(comment_stack) > 0:
        comments = comment_stack.pop()
        depth = len(comment_stack)
        try:
            comment = comments.next()
            comment_stack.append(comments)
            if type(comment) == praw.objects.MoreComments:
                comment_stack.append(iter(comment.comments()))
                continue
            
            #####  do stuff ######
            space_char = ' ' if args.spaces else '&nbsp;'
            prepend = ('|' + space_char * 3) * depth
            author_line = prepend
            author_line += '[-] ' + comment.author.name if comment.author is not None else '[deleted]'
            author_line += ' %d point' % comment.score
            if comment.score > 1:
                author_line += 's'
            print author_line
            comment_text = html.unescape(markdown_to_bbcode(comment.body))
            for line in comment_text.splitlines():
                print '%s%s' % (prepend, line)
            if len(comment.replies) > 0:
                comment_stack.append(iter(comment.replies))
            print prepend
            ##### /do stuff ######

        except StopIteration:
            continue
    
    
if __name__ == '__main__':
    main()
