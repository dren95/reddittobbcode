# REDDITTOBBCODE

    usage: reddittobbcode.py [-h] [-s] submission_id
     
    Prep reddit submission w/ comments for posting on bbcode forum. Comment
    hierarchy is preserved and markdown syntax is converted to bbcode where
    possible.
     
    positional arguments:
      submission_id  reddit base 36 submission id
     
    optional arguments:
      -h, --help     show this help message and exit
      -s             spaces instead of &nbsp;

## Installing

Clone this repo then

    $ virtualenv ENV
    $ . ENV/bin/activate
    $ pip install -r requirements.txt

After praw and the other dependencies install you are good to go.

To deactivate the virtualenv do

    $ deactivate

## Example usage
Find a reddit post and extract the submission id from the url, e.g.
http://www.reddit.com/r/Bitcoin/comments/27sa4v/im_curious_about_bitcoin_and_im_a/ has a submission id of 27sa4v. Supply the submission id to the program:

    $ python reddittobbcode.py -s 27sa4v

    [url=http://www.reddit.com/r/Bitcoin/comments/27sa4v/im_curious_about_bitcoin_and_im_a/]I'm curious about Bitcoin and I'm a _______.[/url]
    submitted by solomania9
     
    I think this would be a great educational Bitcoin website. It would be a list of about 15 archetypes (such as Banker, Web Designer, Stay-at-home Mom, Factory Worker, etc...). 
     
    When you click on each one, you'd get a brief customized tutorial/overview that matches your vocabulary and interests.
     
    Bitcoin can be explained in so many ways to so many different people, so why don't we start doing it that way?
     
    Does anything like this already exist?
     
     
     
    [-] BitcoinOdyssey 6 points
    Ya….good idea  + multiple languages
     
    [-] ISkiAtAlta 14 points
    > I'm curious about bitcoin and I'm a ______  
     
    "girl" is what we were all hoping for. 
     
    |   [-] ferroh 14 points
    |   That option replies with OP's phone number.
    |   
    |   [-] vdogg89 1 point
    |   "Sorry, there is no relevant information on that topic"
    |   
    [-] lewisjackson 5 points
    We could start an open source effort and host it on GitHub pages?
     
    [-] b44rt 3 points
    upvoted, hope you get somewhere with this
     
    [-] grape_damn_popsicle 2 points
    I'm curious about Bitcoin and I'm a lesbian midget left-handed Eskimo albino.
     
    |   [-] moronmonday526 2 points
    |   "That wiki page does not exist. Click <here> to create it!"
    |   
    [-] cg164 2 points
    Is it bad to steal some ones idea I wonder...
     
    |   [-] solomania9 3 points
    |   By all means go for it!
    |   
    |   [-] SingularityLoop 2 points
    |   No, results are all that matter he wouldn't post it publicly if this was a concern.  
    |   
    [-] jgrad 2 points
    It'd be extremely useful for people who are, for instance, immigrants attempting to send money back home. Or small businesses that sell things online.
     
    But it's hard to see how it'd be useful for things any more specific than that. 
     
    [-] smithd98 1 point
    I've got a project in the beta stage along those lines. Not ready for launch yet, but here is a preview. I'd love to get feedback: http://www.sowhatsbitcoin.com/
     
    |   [-] solomania9 2 points
    |   I think it's great! It's a really nice approachable bird's eye view.
    |   
    |   You might also want to mention Coinbase for merchants. I use them for http://bitcoinmegaphone.com and have been relatively happy.
    |   
    [-] targetpro 1 point
    Haven't seen this done yet.  Fantastic idea though.  Get a good domain name and Go For It!
     
    [-] DidHeJust 1 point
    Working on something like this on the back end with spare time, anyone want to contribute content and do write-ups?/Idea talk?
     
    [-] bitappend 1 point
    i actually already did these 
     
    [-] petskup 1 point
    I'm curious about bitcoin and I'm a dumb :)
     
    [-] bankerfrombtc -3 point
    This is a genius idea only because it'd be the funniest thing in history to watch a bitcoiner try to write to a stay at home mom or banker or factory worker about their vocabulary and interests. 
     
    |   [-] ostracize 1 point
    |   You know how your kids are unique and there are no other kids exactly the same as them? Think of you bitcoin addresses as your kids. Unique and cannot be duplicated.
    |   
    |   ...
    |   
    |   You know how your kids goes to school and trades their banana for a Snack Pack? Think of it as a transferring bitcoins from one address to another.
    |   
    |   ...
    |   
    |   |   [-] aletoledo 1 point
    |   |   Whats cute about your comment is that these are like the last thing they care about. not sure if you did that on purpose or not.
    |   |   
    |   [-] solomania9 1 point
    |   "Hi fellow mom. Don't you love your kids? Know what else you should love? Bitcoin..."
    |   
    |   Really though, the best way to do it would be to enlist freelance writers who actually fit the demographic for each category.
    |   
    |   |   [-] khai42 0 point
    |   |   Fiverr?
    |   |   
    [-] supremecommand3r -2 point
    Girls obese