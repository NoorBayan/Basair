import pandas as pd
from topic_template import *
from IPython.display import display, HTML
w = pd.read_csv("corpus/QuranTopics.csv", sep='\t', encoding='utf-16')
arw={w.en_words.iloc[i]:w.ar_words.iloc[i] for i in range(len(w))}
cost={w.en_words.iloc[i]:w.cost.iloc[i] for i in range(len(w))}
wlevel={w.en_words.iloc[i]:w.wlevel.iloc[i] for i in range(len(w))}
ypos={w.en_words.iloc[i]:w.pos.iloc[i] for i in range(len(w))}

def up_tree(topic):
    ut=w[w.en_words==topic].parint.iloc[0]
    if ut!='_':
        up_tree(ut)
        upt.append(ut)

def get_tree(topic,x):
    e=[]
    #topics=0
    p=w[w.parint==topic]
    if len(p)>0:
        topics=list(p.en_words)
    c=[cost[i] for i in topics]
    d=250
    size=sum(c)*d
    start=x-(size/2)
    s=[d*i for i in c]
    p=start
    for i in s:
        p=i+p
        e.append(p-(i/2))
    return topics,e
class TopicsMapRenderer(object):
    """Render topics map as SVGs."""
    style = 'dep'

    def __init__(self, options={}):
        """Initialise dependency renderer.
        options (dict): Visualiser-specific options (compact, word_spacing,
            arrow_spacing, arrow_width, arrow_stroke, distance, offset_x,
            color, bg, font)
        """
        self.compact = options.get('compact', True)
        self.word_spacing = options.get('word_spacing', 30)
        self.box_width = options.get('box_width', 200)
        self.box_height = options.get('box_height', 70)
        self.box_x_shift = options.get('box_x_shift', self.box_width/2)
        self.vlin_height = options.get('vlin_height', 30)
        self.en_text_shift = options.get('en_text_shift',25)
        self.ar_text_shift = options.get('ar_text_shift',55)
        self.distance = options.get('distance', 50 if self.compact else 130)
        self.offset_x = options.get('offset_x', 20)
        self.color = options.get('color', '#000000')
        self.bg = options.get('bg', '#ffffff')
        self.font = options.get('font', 'KFGQPC HafsEx1 Uthmanic Script')  
        
    def render_map_svg(self, render_id,topic):
        """Render SVG.
        render_id (int): Unique ID, typically index of document.
        words (list): Individual words and their tags.
        arcs (list): Individual arcs and their start, end, direction and label.
        RETURNS (unicode): Rendered SVG markup.
        """
        content=""
        c=cost[topic]
        l=wlevel[topic]
        up_tree(topic)
        self.bord_width=(c*self.box_width)+(c*self.distance)+self.offset_x
        self.bord_height=660
        x = self.bord_width/2
        up_levels,y=self.render_up_tree(10,x)
        curent_node,y=self.render_curent_node(topic,y,x)
        topics,e=get_tree(topic,x)
        #down_tree=''
        down_tree=self.render_down_tree(topics,e,y,x,[])
        down_trees=''
        content = ''.join(up_levels) + ''.join(curent_node)+ ''.join(down_tree)
        return TPL_ONT_SVG.format(id=render_id, width=self.bord_width,
                                  height=self.bord_height, color=self.color,
                                  bg=self.bg, font=self.font, content=content)

    def render_up_tree(self,y,x):
        """Render SVG.
        render_id (int): Unique ID, typically index of document.
        words (list): Individual words and their tags.
        arcs (list): Individual arcs and their start, end, direction and label.
        RETURNS (unicode): Rendered SVG markup.
        """
        content=""
        y1=y+self.en_text_shift
        y2=y+self.ar_text_shift
        for i in upt:
            box  = TPL_TOP_BOX.format(width=self.box_width,height=self.box_height,x=x-self.box_x_shift,y=y,
                                tcolor='black',x1=x, y1=y1,y2=y2,etext=i,atext=arw[i])
            
            y=y+self.box_height
            
            vlin = TPL_LIN_VER.format(x=x,y1=y,y2=y+self.vlin_height)
            y=y+self.vlin_height
            y1=y+self.en_text_shift
            y2=y+self.ar_text_shift

            content =content + ''.join(box) + ''.join(vlin)
        return content,y

    def render_curent_node(self,topic,y,x):
        """Render SVG.
        render_id (int): Unique ID, typically index of document.
        words (list): Individual words and their tags.
        arcs (list): Individual arcs and their start, end, direction and label.
        RETURNS (unicode): Rendered SVG markup.
        """
        y1=y+self.en_text_shift
        y2=y+self.ar_text_shift
        box  = TPL_TOP_BOX.format(width=self.box_width,height=self.box_height,x=x-self.box_x_shift,y=y,
                    tcolor='blue',x1=x, y1=y1,y2=y2,etext=topic,atext=arw[topic])
        return box,y2

    def render_down_tree(self,topics,e,y,x,content):
        """Render SVG.
        """
        content.append(self.draw_down_tree(topics,y,x,e))
        for i in range(len(topics)):
            if cost[topics[i]]>1:
                a,b=get_tree(topics[i],e[i])
                self.render_down_tree(a,b,y,e[i],content)
        return content
    
    def draw_down_tree(self,topics,y,x,xp):
        """Render SVG.
        """
        y=ypos[topics[0]]-15
        vlint  = TPL_LIN_VER.format(x=x,y1=y-15,y2=y)
        
        hline =TPL_LIN_HOR.format(x1=xp[0],x2=xp[-1],y1=y,y2=y)
        vlins=''
        for i in range(len(xp)):
            vlin  = TPL_LIN_VER.format(x=xp[i],y1=y,y2=y+15)
            box  = TPL_TOP_BOX.format(width=self.box_width,height=self.box_height,x=xp[i]-self.box_x_shift,y=y+15,
            tcolor='blue',x1=xp[i], y1=y+40,y2=y+70,etext=topics[i],atext=arw[topics[i]])
            vlins =vlins +  ''.join(vlin)+  ''.join(box)
        content = ''.join(vlint) + ''.join(hline) + ''.join(vlins)
        return content

    
def concept_map(topic):
    global upt
    upt=[]
    html = TopicsMapRenderer()
    htm = html.render_map_svg(1,topic)
    return htm
def draw_concept_map(topic):
    htm=concept_map(topic)
    return display(HTML(htm))


########### story
class TopicsStoryRenderer(object):
    """Render topics map as SVGs."""
    style = 'dep'

    def __init__(self, options={}):
        """Initialise dependency renderer.
        options (dict): Visualiser-specific options (compact, word_spacing,
            arrow_spacing, arrow_width, arrow_stroke, distance, offset_x,
            color, bg, font)
        """
        self.compact = options.get('compact', True)
        self.box_width = options.get('box_width', 200)
        self.color = options.get('color', '#000000')
        self.bg = options.get('bg', '#ffffff')
        self.font = options.get('font', 'KFGQPC HafsEx1 Uthmanic Script')  
        
    def render_story(self, render_id,title,story,moral,question,answer):
        """Render SVG.
        render_id (int): Unique ID, typically index of document.
        words (list): Individual words and their tags.
        arcs (list): Individual arcs and their start, end, direction and label.
        RETURNS (unicode): Rendered SVG markup.
        """
        s=""; m="";q="";a=""
        for i in story:
            ss=TPL_PRAG.format(kids=i)
            s=s +''.join(ss)
        for i in moral:
            mm=TPL_PRAG.format(kids=i)
            m=m +''.join(mm)
        for i in question:
            qq=TPL_PRAG.format(kids=i)
            q=q +''.join(qq)
        for i in answer:
            aa=TPL_PRAG.format(kids=i)
            a=a +''.join(aa)
        

        return TPL_STORY.format(id=render_id, title=title, story=s, moral=m, question=q, answer=a)
def get_story_info(title):
    story = pd.read_csv("Corpus/story.csv", sep='\t', encoding='utf-16')
    s=story[story.title==title]
    title=list(s.title)[0]
    story=[i.split('\n') for i in list(s.story) if i.split('\n')!=''][0]
    story=[i for i in story if i!='']
    moral=[i.split('\n') for i in list(s.moral) if i.split('\n')!=''][0]
    question=[i.split('\n') for i in list(s.question) if i.split('\n')!=''][0]
    answer=[i.split('\n') for i in list(s.answer) if i.split('\n')!=''][0]
    return title,story,moral,question,answer

def quran_story(title):
    title,story,moral,question,answer = get_story_info(title)
    html = TopicsStoryRenderer()
    htm = html.render_story(1,title,story,moral,question,answer )
    return htm

def get_quran_story(title):
    htm=quran_story(title)
    return display(HTML(htm))
