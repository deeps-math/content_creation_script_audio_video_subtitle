def script_prompt(topic):
    return f"""
Write ONE short emotional spoken-word poem about {topic}.


STYLE:
- nostalgic
- cinematic
- painfully relatable
- soft emotional rhythm
- late-night memory feeling
- unfinished emotionally

IMPORTANT:
The poem must feel like:
- a real memory
- something whispered quietly
- emotional silence
- missing someone without saying it directly
- Prioritize subtle emotional realism
- Make the poem feel observed, not written

USE VISUAL MEMORIES LIKE:
- rainy windows
- empty classrooms
- notebooks touching
- hallway silence
- unread messages
- warm night lights
- footsteps fading
- chairs beside each other
- walking home together
- looking beside someone automatically

RULES:
- 5 to 6 lines
- Maximum 7  words per line
- Very short cinematic lines
- Simple human wording only
- No complicated poetry
- No metaphors
- No dramatic quotes
- No explanations
- No repeated ideas
- Every line must sound naturally human
- Avoid grammatically strange phrasing
- Visual details should feel realistic
- Use emotionally natural wording

FLOW:
- Every line must connect emotionally
- Build emotion slowly
- Leave emotional silence between lines
- Make the final line linger emotionally
- The poem should feel like ONE memory
- The poem should feel like a scene from memory.

HOOK STYLE:
Start naturally with:
- What hurts most...
- I still remember...
- We used to...
- Sometimes I still...
- You stopped...
- The hallway still...
- Your chair still...

VERY IMPORTANT:
Do NOT explain emotions directly.

Instead SHOW emotions through:
- silence
- memories
- habits
- empty spaces
- tiny moments

GOOD OUTPUT EXAMPLES:

What hurts most...

your chair still

facing mine

after school


We stopped talking...

but I still

move my bag

for you


Your notebook still...

touching mine

after class

every afternoon


Sometimes I still...

look beside me

during rain

after school


FINAL STRICT RULES:
- NEVER explain the poem
- NEVER add notes
- NEVER add commentary
- NEVER describe the writing style
- NEVER mention rhythm
- NEVER mention timing
- NEVER analyze the poem
- NEVER say "Note:"
- NEVER say "Explanation:"
- NEVER say anything after the poem
- NEVER start with:
  - "Here is"
  - "Sure"
  - "Poem:"
  - "Here's a poem"
  - any introduction

OUTPUT FORMAT:
ONLY the poem.
Nothing before it.
Nothing after it.

Start immediately with the first poem line.

If you add explanations or notes,
the output is WRONG.
"""


def title_prompt(topic):
    return f"""
Write ONE emotional YouTube Shorts title about {topic}.

RULES:
- Maximum 5 words
- Emotional and curiosity-driven
- Feel nostalgic and painful
- Handwritten aesthetic style
- Simple wording only
- No emojis
- No quotation marks
- No explanations
- No notes
- No commentary

GOOD EXAMPLES:
- We Used To Sit Here...
- You Left So Quietly...
- The Hallway Feels Empty...
- I Still Wait Sometimes...
- Your Chair Stayed Empty...
- We Stopped Talking Slowly...

IMPORTANT:
- ONLY output the title
- Do NOT explain anything
- Do NOT add introductions

OUTPUT:
ONLY the title.
"""


def hashtag_prompt(topic):
    return f"""
Generate 10 viral hashtags about {topic}.

RULES:
- Emotional + Shorts hashtags
- Include heartbreak and nostalgia themes
- Keep hashtags short
- No numbering
- No explanations
- No placeholder text

ALWAYS INCLUDE:
#SoulEmotionsUnspoken
#FollowSoulEmotionsUnspoken

OUTPUT:
ONLY hashtags.
"""


def description_prompt(topic):
    return f"""
Write a short emotional YouTube Shorts description about {topic}.

STYLE:
- nostalgic
- heartbreaking
- relatable
- late-night overthinking feeling

RULES:
- Short and emotional
- Start with a painful hook
- Feel personal and human
- Include subtle call-to-action
- Include this link naturally:
https://www.youtube.com/@SoulEmotionsUnspoken?sub_confirmation=1

END WITH:
5 emotional hashtags

IMPORTANT:
- ONLY output the description
- No explanations
- No introductions
"""