import requests
import json

def generate_image(prompt, filename):
    api_url = "https://image.pollinations.ai/prompt/"
    full_url = f"{api_url}{prompt}"

    try:
        response = requests.get(full_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully saved '{filename}' for prompt: '{prompt}'")

    except requests.exceptions.RequestException as e:
        print(f"Error generating image for prompt '{prompt}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred for prompt '{prompt}': {e}")

# Define the list of shows with their prompts and filenames
shows_data = [
    {
        "Show": "& Juliet",
        "Prompt": "A vibrant, pop-art style image of Juliet with a microphone, surrounded by bright colors. The tone should be fun and modern.",
        "Filename": "and-juliet.jpg"
    },
    {
        "Show": "Aladdin",
        "Prompt": "A magical, Disney-style image of Aladdin and Jasmine on a flying carpet over a starry desert city. The mood is adventurous and romantic.",
        "Filename": "aladdin.jpg"
    },
    {
        "Show": "Art on Broadway",
        "Prompt": "Three people looking at a minimalist, white canvas. The style is modern and slightly dramatic, with a focus on human expression.",
        "Filename": "art-on-broadway.jpg"
    },
    {
        "Show": "Buena Vista Social Club",
        "Prompt": "An atmospheric, vintage-style photo of musicians playing Cuban music in a lively, old Havana street. The colors are warm and nostalgic.",
        "Filename": "buena-vista-social-club.jpg"
    },
    {
        "Show": "Cabaret at the Kit Kat Club",
        "Prompt": "A provocative, dimly lit image of a cabaret singer with bold makeup and a microphone, with a dark, smoky nightclub background.",
        "Filename": "cabaret.jpg"
    },
    {
        "Show": "Chicago",
        "Prompt": "A black and white, Art Deco-style image of two women in flapper dresses, holding microphones, with a striking city skyline in the background. The mood is sleek and glamorous.",
        "Filename": "chicago.jpg"
    },
    {
        "Show": "Death Becomes Her",
        "Prompt": "A fantastical, dark comedy-themed image of two rival actresses fighting over a bottle of potion, with a hint of magical effects.",
        "Filename": "death-becomes-her.jpg"
    },
    {
        "Show": "Hadestown",
        "Prompt": "A dramatic, atmospheric image of a folk/jazz band in a dark, industrial-looking underworld, with a single, warm light source on the characters.",
        "Filename": "hadestown.jpg"
    },
    {
        "Show": "Hamilton",
        "Prompt": "A dynamic, historical-yet-modern portrait of Alexander Hamilton and other founding fathers in hip-hop poses, with a backdrop of a colonial city.",
        "Filename": "hamilton.jpg"
    },
    {
        "Show": "Harry Potter and the Cursed Child",
        "Prompt": "A mysterious, magical image of a boy standing on a train track, surrounded by swirling magical energy. The tone is dark and fantastical.",
        "Filename": "harry-potter.jpg"
    },
    {
        "Show": "Hell's Kitchen",
        "Prompt": "A vibrant, street art-inspired image of a young girl with headphones, dancing in a bustling New York City neighborhood.",
        "Filename": "hells-kitchen.jpg"
    },
    {
        "Show": "Jeff Ross: Take a Banana For the Ride",
        "Prompt": "A comedy show poster featuring Jeff Ross with a microphone and a mischievous grin, with a banana prop.",
        "Filename": "jeff-ross.jpg"
    },
    {
        "Show": "Just in Time",
        "Prompt": "A modern, romantic comedy-style image of a couple looking at their phones with a city backdrop. The mood is light and contemporary.",
        "Filename": "just-in-time.jpg"
    },
    {
        "Show": "Little Shop of Horrors",
        "Prompt": "A vintage-style horror-comedy image of a man holding a carnivorous, singing plant with a terrified expression. The colors are garish and fun.",
        "Filename": "little-shop.jpg"
    },
    {
        "Show": "Mamma Mia!",
        "Prompt": "A sunny, joyful image of three women dancing on a Greek island, surrounded by vibrant colors. The theme is ABBA and good times.",
        "Filename": "mamma-mia.jpg"
    },
    {
        "Show": "Maybe Happy Ending",
        "Prompt": "A whimsical, animated-style image of two rusty, old robots sitting together on a bench, looking at a futuristic city in the distance.",
        "Filename": "maybe-happy-ending.jpg"
    },
    {
        "Show": "MJ The Musical",
        "Prompt": "A powerful, theatrical image of a dancer in a Michael Jackson-inspired pose, with a spotlight on them and a concert stage background.",
        "Filename": "mj-the-musical.jpg"
    },
    {
        "Show": "Moulin Rouge! The Musical",
        "Prompt": "A spectacular, romantic image of a couple dancing in a red-drenched, opulent nightclub with a large windmill in the background.",
        "Filename": "moulin-rouge.jpg"
    },
    {
        "Show": "Oh, Mary!",
        "Prompt": "A comedic, historical image of a young Abraham Lincoln in a funny pose, with a spotlight on him and a hint of a political setting.",
        "Filename": "oh-mary.jpg"
    },
    {
        "Show": "Operation Mincemeat",
        "Prompt": "A retro, WWII-era spy movie poster-style image with a comedic twist, featuring secret agents and a map.",
        "Filename": "operation-mincemeat.jpg"
    },
    {
        "Show": "Punch",
        "Prompt": "A dramatic, minimalist image of a single person on a dark stage, with a spotlight on them, representing a new play.",
        "Filename": "punch.jpg"
    },
    {
        "Show": "SIX: The Musical",
        "Prompt": "A pop-music, concert-style image of six women in queen-like outfits, each with a different color theme, holding microphones on a stage.",
        "Filename": "six.jpg"
    },
    {
        "Show": "Stranger Things: The First Shadow",
        "Prompt": "A dark and mysterious image of a young boy's silhouette with a shadow looming behind him, evoking the style of the Stranger Things series.",
        "Filename": "stranger-things.jpg"
    },
    {
        "Show": "The Book of Mormon",
        "Prompt": "A colorful, satirical cartoon image of two Mormon missionaries in a foreign country, looking surprised and comical.",
        "Filename": "the-book-of-mormon.jpg"
    },
    {
        "Show": "The Great Gatsby",
        "Prompt": "A glamorous, 1920s Art Deco image of a lavish party scene, with a couple dancing and fireworks in the background.",
        "Filename": "the-great-gatsby.jpg"
    },
    {
        "Show": "The Lion King",
        "Prompt": "A stunning, African savanna-inspired image of a lion cub on Pride Rock, with a majestic sun setting in the background. The style should be theatrical and beautiful.",
        "Filename": "the-lion-king.jpg"
    },
    {
        "Show": "The Outsiders",
        "Prompt": "A gritty, 1950s-era image of a group of teenagers in leather jackets, standing together in a tough neighborhood. The tone is emotional and dramatic.",
        "Filename": "the-outsiders.jpg"
    },
    {
        "Show": "Wicked",
        "Prompt": "A whimsical and magical image of two witches, one green and one good, flying in the sky over the Land of Oz. The mood is epic and fantastical.",
        "Filename": "wicked.jpg"
    },
    {
        "Show": "Rob Lake Magic with Special Guests The Muppets",
        "Prompt": "A family-friendly magic show poster featuring a magician and a couple of Muppets characters doing a trick.",
        "Filename": "rob-lake-magic.jpg"
    },
    {
        "Show": "Heathers The Musical",
        "Prompt": "A cult classic musical poster, with teenagers in a high school setting, hinting at a dark comedy.",
        "Filename": "heathers.jpg"
    },
    {
        "Show": "Prince F*ggot",
        "Prompt": "An edgy, minimalist play poster with a striking, dark design.",
        "Filename": "prince-faggot.jpg"
    },
    {
        "Show": "Ginger Twinsies",
        "Prompt": "A fun, comedic image of two redheaded twins in a stand-up comedy setting.",
        "Filename": "ginger-twinsies.jpg"
    },
    {
        "Show": "AMAZE Magic",
        "Prompt": "A mind-bending magic and illusion show poster, with swirling colors and magical effects.",
        "Filename": "amaze-magic.jpg"
    },
    {
        "Show": "Color Theories by Julio Torres",
        "Prompt": "A surreal comedy special poster, with a comedian in a colorful, whimsical setting.",
        "Filename": "color-theories.jpg"
    },
    {
        "Show": "Queen of Hearts by Company XIV",
        "Prompt": "A decadent, burlesque-style show poster, with a performer in a lavish, theatrical costume.",
        "Filename": "queen-of-hearts.jpg"
    },
    {
        "Show": "Pen Pals",
        "Prompt": "A touching and funny play poster, showing two people from different worlds writing letters to each other.",
        "Filename": "pen-pals.jpg"
    },
    {
        "Show": "The Play That Goes Wrong",
        "Prompt": "A hilarious farce poster, showing a disastrous murder mystery play in chaos.",
        "Filename": "play-that-goes-wrong.jpg"
    },
    {
        "Show": "The Other Americans",
        "Prompt": "A dramatic play poster about the immigrant experience.",
        "Filename": "the-other-americans.jpg"
    },
    {
        "Show": "Monkey Off My Back or The Cat’s Meow",
        "Prompt": "A surreal, experimental play poster with a whimsical twist.",
        "Filename": "monkey-off-my-back.jpg"
    },
    {
        "Show": "House of McQueen",
        "Prompt": "A biographical play poster about fashion designer Alexander McQueen.",
        "Filename": "house-of-mcqueen.jpg"
    },
    {
        "Show": "Mexodus",
        "Prompt": "A powerful musical poster about stories of migration.",
        "Filename": "mexodus.jpg"
    },
    {
        "Show": "Drunk Romeo & Juliet",
        "Prompt": "A boisterous, improvised play poster with a comical, chaotic take on a Shakespeare classic.",
        "Filename": "drunk-romeo-and-juliet.jpg"
    },
    {
        "Show": "Ava: The Secret Conversations",
        "Prompt": "A revealing play poster about Hollywood legend Ava Gardner, with a noir-inspired aesthetic.",
        "Filename": "ava.jpg"
    },
    {
        "Show": "Perfect Crime",
        "Prompt": "A classic whodunit murder mystery poster with a detective and a dramatic scene.",
        "Filename": "perfect-crime.jpg"
    },
    {
        "Show": "Exorcistic: The Rock Musical",
        "Prompt": "A parody horror rock musical poster, with a campy, theatrical design.",
        "Filename": "exorcistic.jpg"
    },
    {
        "Show": "Friends The Musical Parody",
        "Prompt": "A hilarious musical parody poster, inspired by the TV sitcom Friends.",
        "Filename": "friends.jpg"
    },
    {
        "Show": "This is Government",
        "Prompt": "A thought-provoking play poster about modern bureaucracy.",
        "Filename": "this-is-government.jpg"
    },
    {
        "Show": "Cocktail Magique by Company XIV",
        "Prompt": "A lavish, theatrical cocktail experience poster, with burlesque and magic elements.",
        "Filename": "cocktail-magique.jpg"
    },
    {
        "Show": "Sober Songs",
        "Prompt": "A moving one-man show poster about a musician's journey to sobriety.",
        "Filename": "sober-songs.jpg"
    },
    {
        "Show": "New York Comedy Club (Upper West Side)",
        "Prompt": "A classic NYC comedy club poster with a brick wall and a comedian on stage.",
        "Filename": "nyc-comedy-club-uws.jpg"
    },
    {
        "Show": "Gazillion Bubble Show",
        "Prompt": "A captivating spectacle poster for a bubble show, with light and laser effects.",
        "Filename": "gazillion-bubble-show.jpg"
    },
    {
        "Show": "Chamber Magic",
        "Prompt": "An elegant, intimate magic show poster in a close-up setting.",
        "Filename": "chamber-magic.jpg"
    },
    {
        "Show": "New York Comedy Club (Midtown)",
        "Prompt": "A classic NYC comedy club poster with a brick wall and a comedian on stage.",
        "Filename": "nyc-comedy-club-midtown.jpg"
    },
    {
        "Show": "The Office! A Musical Parody",
        "Prompt": "A musical parody poster inspired by The Office TV series.",
        "Filename": "the-office.jpg"
    },
    {
        "Show": "New York Comedy Club (East Village)",
        "Prompt": "A classic NYC comedy club poster with a brick wall and a comedian on stage.",
        "Filename": "nyc-comedy-club-ev.jpg"
    },
    {
        "Show": "The Infinite Wrench",
        "Prompt": "A chaotic, fast-paced performance poster with many short plays.",
        "Filename": "infinite-wrench.jpg"
    },
    {
        "Show": "Galas",
        "Prompt": "A sophisticated, one-night-only performance and event poster.",
        "Filename": "galas.jpg"
    },
    {
        "Show": "This is Not a Drill",
        "Prompt": "A high-energy, immersive theatrical experience poster.",
        "Filename": "this-is-not-a-drill.jpg"
    },
    {
        "Show": "Cracked Open",
        "Prompt": "An emotional and raw new play poster.",
        "Filename": "cracked-open.jpg"
    },
    {
        "Show": "Sleepy Hollow the Musical",
        "Prompt": "A musical adaptation poster of the classic American ghost story.",
        "Filename": "sleepy-hollow.jpg"
    },
    {
        "Show": "The Divine Dating Game",
        "Prompt": "A comedic and interactive show poster about finding love.",
        "Filename": "divine-dating-game.jpg"
    },
    {
        "Show": "ApocaLIPSTICK",
        "Prompt": "A drag and comedy show poster about the end of the world.",
        "Filename": "apocalipstick.jpg"
    },
    {
        "Show": "Queens",
        "Prompt": "A new play poster about women navigating life and power.",
        "Filename": "queens.jpg"
    },
    {
        "Show": "From Trinity to Trinity",
        "Prompt": "An experimental theatre piece poster.",
        "Filename": "from-trinity-to-trinity.jpg"
    },
    {
        "Show": "Katsura Sunshine’s Rakugo",
        "Prompt": "A solo show poster of traditional Japanese comedic storytelling.",
        "Filename": "katsura-sunshine.jpg"
    },
    {
        "Show": "59E59 Theaters",
        "Prompt": "A collective discount poster for shows at the off-Broadway theater.",
        "Filename": "59e59-theaters.jpg"
    },
    {
        "Show": "Waiting For Godot",
        "Prompt": "A classic existentialist play poster with a simple, stark design.",
        "Filename": "waiting-for-godot.jpg"
    }
]

# Loop through each show and generate an image
for show in shows_data:
    generate_image(show["Prompt"], show["Filename"])
