import random

class QuotesDB:
    def __init__(self) -> None:
        pass
    
    list = [
            ["Children are not things to be molded, but are people to be unfolded.","Jess Lair"],
            ["A child is a beam of sunlight from the Infinite and Eternal, with possibilities of virtue and vice, but as yet unstained.","Lyman Abbott"],
            ["Children are the living messages we send to a time we will not see.","John F. Kennedy"],
            ["The soul is healed by being with children.","Fyodor Dostoyevsky"],
            ["Children are like wet cement: whatever falls on them makes an impression.","Haim Ginot"],
            ["The best inheritance a parent can give his children is a few minutes of his time each day.","Orlando Aloysius Battista"],
            ["Children have never been very good at listening to their elders, but they have never failed to imitate them.","James Baldwin"],
            ["The potential possibilities of any child, are the most intriguing and stimulating in all creation.","Ray L. Wilbur"],
            ["The best way to make children good, is to make them happy","Oscar Wilde"],
            ["When I approach a child, he inspires in me two sentiments – tenderness for what he is and respect for what he may become.","Louis Pasteur"],
            ["The greatest gifts you can give your children are the roots of responsibility and the wings of independence.","Denis Waitley"],
            ["At every step the child should be allowed to meet the real experience of life; the thorns should never be plucked from his roses.","Ellen Key"],
            ["Children see magic because they look for it.","Christopher Moore"],
            ["I have found the best way to give advice to your children is to find out what they want and then advise them to do it.","Harry S. Truman"],
            ["Children are likely to live up to what you believe of them.","Lady Bird Johnson"],
            ["Children must be taught how to think, not what to think.","Margaret Mead"],
            ["Each day of our lives we make deposits in the memory banks of our children.","Charles R. Swindoll"],
            ["Children need models rather than critics.","Joseph Joubert"],
            ["Children need models rather than critics.","Joseph Joubert"],
            ["Children are great imitators. So give them something great to imitate.","Anonymous"],
            ["While we try to teach our children all about life, our children teach us what life is all about.","Angela Schwindt"],
            ["Play is often talked about as if it were a relief from serious learning. But for children play is serious learning. Play is really the work of childhood.","Fred Rogers"],
            ["Our heritage and ideals, our code and standards – the things we live by and teach our children – are preserved or diminished by how freely we exchange ideas and feelings.","Walt Disney"],
            ["There can be no keener revelation of a society’s soul, than the way in which it treats its children.","Nelson Mandela"],
            ["Every child comes with the message that God is not yet discouraged of man.","Rabindranath Tagore"],
            ["If you want your children to be intelligent, read them fairy tales. If you want them to be more intelligent, read them more fairy tales.","Albert Einstein"],
            ["I continue to believe that if children are given the necessary tools to succeed, they will succeed beyond their wildest dreams.","David Vitter"],
            ["A child is a curly dimpled lunatic.","Ralph Waldo Emerson"],
            ["There are two lasting bequests we can give our children. One is roots. The other is wings.","Hodding Carter Jr."],
            ["Like stars are to the sky, so are the children to our world. They deserve to shine!","Chinonye J. Chidolue"],
            ["And I learned what is obvious to a child. That life is simply a collection of little lives, each lived one day at a time. That each day should be spent finding beauty in flowers and poetry and talking to animals. That a day spent with dreaming and sunsets and refreshing breezes cannot be bettered.","Nicholas Sparks"],
            ["I think, at a child’s birth, if a mother could ask a fairy godmother to endow it with the most useful gift, that gift would be curiosity.","Eleanor Roosevelt"],
            ["There is a place where grandmothers hold babies on their laps, under the stars and whisper in their ears that the lights in the sky are holes in the floor of heaven.","Rick Bragg"],
            ["A happy kid has shining eyes. It walks open-hearted into the world and spreads magic.","Sigrid Leo"],
            ["Children are one third of our population and all of our future.","Select Panel for the Promotion of Child Health, 1981"],
            ["History will judge us by the difference we make in the everyday lives of children.","Nelson Mandela"],
            ["Children will listen to you after they feel listened to.","Jane Nelsen"],
            ["You are the bows from which your children as living arrows are sent forth.","Kahlil Gibran"],
            ["Children learn more from what you are, than what you teach.","Du Bois"],
            ["A child is an uncut diamond.","Austin O’Malley"],
            ["Don’t handicap your children by making their lives easy.","Robert A. Heinlein"],
            ["Tell me what’s more important than being present for children and listening to them. I’ll wait.","Maxime Lagacé"],
            ["Children are mirrors, they reflect back to us all we say and do.","Pam Leo"],
            ["If you want your children to turn out well, spend twice as much time with them and half as much money.","Abigail Van Buren"],
            ["Let parents bequeath to their children not riches, but the spirit of reverence.","Plato"],
            ["Even if people are still very young, they shouldn’t be prevented, from saying what they think.","Anne Frank"],
            ["To every child – I dream of a world where you can laugh, dance, sing, learn, live in peace and be happy.","Malala Yousafzai"],
            ["Our most important task as a nation, is to make sure all our young people can achieve their dreams.","Barack Obama"],
            ["We worry about what a child will become tomorrow, yet we forget that he is someone today.","Stacia Tauscher"],
            ["A child seldom needs a good talking to as a good listening to.","Robert Brault"],
            ["Seven things every child needs to hear: I love you, I’m proud of you, I’m sorry, I forgive you, I’m listening. This is your responsibility. You have what it takes to succeed.","Sherrie Campbell, PhD"],
            ["One generation plants the trees; another gets the shade.","Chinese proverb"],
            ["A child can ask questions that a wise man cannot answer.","Anonymous"],
            ["A child can teach an adult three things… To be happy for no reason. To always be busy with something. And to know how to demand with all his might that which he desires.","Paulo Coelho"],
            ["Always smile back at little children. To ignore them is to destroy their belief that the world is good.","Pam Brown"],
            ["It is a wise father that knows his own child.","William Shakespeare"],
            ["It took me four years to paint like Raphael, but a lifetime to paint like a child.","Pablo Picasso"],
            ["All children are artists. The problem is how to remain an artist once he grows up.","Pablo Picasso"],
            ["A child is not a vase to be filled, but a fire to be lit.","Francois Rabelais"],
            ["It takes a village to raise a child.","African proverb"],
            ["A child miseducated is a child lost.","John F. Kennedy"],
            ["Children re-invent your world for you.","Susan Sarandon"],
            ["An honest man is always a child.","Socrates"],
            ["Noble fathers have noble children.","Euripides"],
            ["You know your children are growing up, when they stop asking you where they came from and refuse to tell you where they’re going.","P. J. O’Rourke"],
            ["Don’t try to make children grow up to be like you, or they may do it.","Russell Baker"],
            ["I continue to believe that if children are given the necessary tools to succeed, they will succeed beyond their wildest dreams!","David Vitter"],
            ["If we don’t stand up for children, then we don’t stand for much.","Marian Wright Edelman"],
            ["If we wish to create a lasting peace we must begin with the children.","Mahatma Gandhi"],
            ["There is a brilliant child locked inside every student.","Marva Collins"],
            ["You know who’s going to build that better world? It’s the youth. Children will do things that are now considered impossible.","Kacey McCallister"],
            ["The essence of our effort to see that every child has a chance, must be to assure each an equal opportunity, not to become equal, but to become different – to realize whatever unique potential of body, mind and spirit he or she possesses.","John Fischer"],
            ["If you make children happy now, you make make them happy twenty years hence by the memory of it.","Anonymous"],
            ["The extra hours you put in today will keep a smile on the faces of your children a few years from now.","Anonymous"],
            ["The child must know that he is a miracle, that since the beginning of the world there hasn’t been, and until the end of the world there will not be, another child like him.","Pablo Casals"],
            ["Today our children are our reflection. Tomorrow they will be our shadows.","Maralee McKee"],
            ["Our job is not to toughen our children up to face a cruel and heartless world. Our job is to raise children who will make the world a little less cruel and heartless.","L.R. Knost"],
            ["Children are the only form of immortality that we can be sure of.","Peter Ustinov"],
            ["Children astound me with their inquisitive minds. The world is wide and mysterious to them, and as they piece together the puzzle of life, they ask ‘Why?’ ceaselessly.","John C. Maxwell"],
            ["Your children make it impossible to regret your past. They’re its finest fruits. Sometimes the only ones.","Anna Quindlen"],
            ["Love children especially, for they too are sinless like the angels; they live to soften and purify our hearts and, as it were, to guide us.","Fyodor Dostoyevsky"],
            ["There is no sound more annoying than the chatter of a child, and none more sad than the silence they leave when they are gone.","Mark Lawrence"],
            ["May what I do flow from me like a river, no forcing and no holding back, the way it is with children.","Rainer Maria Rilke"],
            ["Do not indoctrinate your children. Teach them how to think for themselves, how to evaluate evidence, and how to disagree with you.","Richard Dawkins"],
            ["Children are likely to live up to what you believe of them.","Lady Bird Johnson"],
            ["The way we talk to our children becomes their inner voice.","Peggy O’Mara"],
            ["Children aren’t coloring books. You don’t get to fill them with your favorite colors.","Khaled Hosseini"],
            ["If you as parents cut corners, your children will too. If you lie, they will too."," Marian Wright Edelman"],
            ["The greatest legacy one can pass on to one’s children and grandchildren is not money or other material things accumulated in one’s life, but rather a legacy of character and faith.","Billy Graham"],
            ["The best way to make children good is to make them happy.","Oscar Wilde"],
            ["If you can give your son or daughter only one gift… Let it be enthusiasm.","Bruce Barton"],
            ["Don’t worry that children never listen to you; worry that they are always watching you.","Robert Fulghum"],
            ["Anyone who does anything to help a child is a hero to me.","Fred Rogers"],
            ["Children don’t need much advice, but they really do need to be listened to and not just with half an ear.","Emma Thompson"],
            ["To value his own good opinion, a child has to feel that he is a worthwhile person. He has to have confidence in himself as an individual.","Sidonie Gruenberg"],
            ["Don’t limit a child to your own learning, for he was born in another time.","Rabindranath Tagore"],
            ["A child educated only at school is an uneducated child.","George Santayana"],
            ["Any book that helps a child to form a habit of reading, to make reading one of his deep continuing needs, is good for him.","Maya Angelou"],
            ["Good habits formed at youth make all the difference.","Aristotle"],
            ["Children are made readers in the laps of their parents.","Emilie Buchwald"],
            ["Don’t educate your children to be rich. Educate them to be happy, so they know the value of things, not the price.","Anonymous"],
            ["Make it a rule never to give a child a book you would not read yourself.","George Bernard Shaw"],
            ["Education in the true sense is helping the individual to be mature and free, to flower greatly in love and goodness. That is what we should be interested in, and not in shaping the child according to some idealistic pattern.","Jiddu Krishnamurti"],
            ["I know that we need to directly teach our children the most vital lessons, rather than assume that they’ll be understood.","Galit Breen"],
            ["Learning is a result of listening, which in turn leads to even better listening and attentiveness to the other person. In other words, to learn from the child, we must have empathy, and empathy grows as we learn."," Alice Miller"],
            ["Example is the school of mankind, and they will learn at no other.","Edmund Burke"],
            ["When you read to a child, when you put a book in a child’s hands, you are bringing that child news of the infinitely varied nature of life. You are an Awakener.","Paula Fox"],
            ["Don’t just teach your children to read. Teach them to question what they read. Teach them to question everything.","George Carlin"],
            ["A young child is, indeed, a true scientist, just one big question mark. What? Why? How? I never cease to marvel at the recurring miracle of growth, to be fascinated by the mystery and wonder of this brave enthusiasm.","Victoria Wagner"],
            ["Too often, I think, children are required to write before they have anything to say. Teach them to think and read and talk with self-repression, and they will write because they cannot help it.","Anne Sullivan"],
            ["Too often we give our children answers to remember rather than problems to solve."," Roger Lewin"],
            ["Only children believe they are capable of everything.","Paulo Coelho"],
            ["Pretty much all the honest truth telling, there is in the world is done by children.","Oliver Wendell Holmes"],
            ["Kids deserve the right to think, that they can change the world.","Lois Lowry"],
            ["How is it that little children are so intelligent and men so stupid? It must be education that does it.","Alexandre Dumas"],
            ["Childhood means simplicity. Look at the world with the child’s eye – it is very beautiful.","Kailash Satyarthi"],
            ["A child thinks that life is really beautiful and that it will become even more beautiful. It is the duty of society to fulfil that expectation.","Robert Muller"],
            ["Observe your children closely: they have often fundamental approaches and answers to the mysteries of life which we have lost as adults.","Robert Muller"],
            ["Children are the true connoisseurs, what’s precious to them has no price, only value.","Bel Kaufman"],
            ["We should all be inspired by children: they don’t care about fear and mistakes.","Maxime Lagacé"],
            ["Children are a wonderful gift. They have an extraordinary capacity to see into the heart of things and to expose sham and humbug for what they are.","Bishop Desmond Tutu"],
            ["Only those who look with the eyes of children can lose themselves in the object of their wonder.","Eberhard Arnold"],
            ["There are no seven wonders of the world in the eyes of a child. There are seven million.","Walt Streightiff"],
            ["Children don’t need “meaning” to get up in the morning. Life is the meaning.","Naval Ravikant"],
            ["The secret of genius is to carry the spirit of the child into old age, which means never losing your enthusiasm.","Aldous Huxley"],
            ["f a child is to keep alive his inborn sense of wonder, he needs the companionship of at least one adult who can share it, rediscovering with him the joy, excitement and mystery of the world we live in.","Rachel Carson"],
            ["Never help a child with a task at which he feels he can succeed.","Maria Montessori"],
            ["When children come into contact with nature, they reveal their strength.","Maria Montessori"],
            ["Early childhood education is the key to the betterment of society.","Maria Montessori"],
            ["Free the child’s potential, and you will transform him into the world.","Maria Montessori"],
            ["Each of us as citizens, has a role to play in creating a better world for our children.","Nelson Mandela"],
            ["Our children are the rock on which our future will be built, our greatest asset as a nation. They will be the leaders of our country, the creators of our national wealth, those who care for and protect our people.","Nelson Mandela"],
            ["The best candy shop a child can be left alone in, is the library.","Maya Angelou"],
            ["That’s the real trouble with the world. Too many people grow up.","Walt Disney"],
            ["The law of love could be best understood and learned through little children.","Mahatma Gandhi"],
            ["If we are to teach real peace in this world, and if we are to carry on a real war against war, we shall have to begin with the children.","Mahatma Gandhi"],
            ["The greatest lessons in life, if we would but stoop and humble ourselves, we would learn not from the grown-up learned men, but from the so-called ignorant children.","Mahatma Gandhi"],
            ["It is vital that when educating our children’s brains, that we do not neglect to educate their hearts.","14th Dalai Lama"], 
            ["Children are our greatest untapped resource.","14th Dalai Lama"],
            ["The visions we offer our children shape the future.","Carl Sagan"],
            ["For these are all our children. We will all profit by, or pay for, whatever they become.","James Baldwin"],
            ["Cherish your children… for they are the footprints you will leave behind.","Taylor Evan Fulks"],
            [" We must teach our children to dream with their eyes open.","Harry Edwards"],
            ["Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them.","Antoine de Saint-Exupéry"], 
            ["Stunt, dwarf, or destroy the imagination of a child, and you have taken away its chances of success in life. Imagination transforms the commonplace into the great and creates the new out of the old.","Frank Baum"],
            ["Children find everything in nothing; men find nothing in everything.","Giacomo Leopardi"],
            ["No one has yet realized the wealth of sympathy, the kindness, and generosity hidden in the soul of a child. The effort of every true education should be to unlock that treasure.","Emma Goldman"],
            ["To me there is no picture so beautiful as smiling, bright-eyed, happy children; no music so sweet as their clear and ringing laughter.","P.T. Barnum"],
            ["It is easier to build strong children than to repair broken men.","Frederick Douglass"],
            ["When you know better, you do better","Maya Angelou"], 
            ["If you want to be more powerful in life, educate yourself. It’s that simple.","Anonymous"],
            ["When you talk, you are only repeating something you know. But if you listen, you may learn something new.","Dalai Lama"],
            ["Learn as much as you can while you are young, since life becomes too busy later","Dana Stewart Scott"],
            ["The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice.","Brian Herbert"],
            ["What is time? -A beautiful horse that is spinning the earth.","Zaika book, Adrian, 5y.o."],
            ["What are weeds? - Weeds are plants that are useful only for themselves.","Zaika book, Daniel, 12y.o."], 
            ["What is betrayal? - Betrayal means a dead friendship.","Zaika book, Adrian, 11y.o."],
            ["What is a home? - A home is where man shelters his life from natural phenomena.","Zaika book, Alexandra, 9y.o."],
            ["What does being patriotic mean? - Patriotic means, when the boss calls his employees to work.","Zaika book,  Jeanina, 8y.o."],
            ["What is a job? - A job is when a person signs a registry book or stays to have a coffee.","Zaika book, Florin, 7y.o."],
            ["What are germs? - Germs are little bugs that are tiny and hidden around the same corner store. When they see that you’ve bought potatoes, they jump onto the potatoes and if you don’t wash them, you’ll die.","Zaika book, Dan, 7y.o."],
            ["What is a drug? - Drugs are a type of plant that gangsters dry up and take as medicine to forget their actions.","Zaika book, 7y.o."], 
            ["What is rebellion? - When our parents can't find money, they start rebelling to find them?","Zaika book, 8 y.o."],
            ["What are the fingerprints? - When you put your hand on the door handle and your fingers remain there and the police find them.","Zaika book, 8y.o."],
            ["What is politics? - Politics is when a lot of people come together and talk too much.","Zaika book, 8y.o."],
            ["What is politics? - Politics is a kind of espionage.","Zaika book, 12y.o."],
            ["What is the celebration of the New Year? -  The celebration of the New Year is when one person goes to another, eats, drinks and gets drunk.","Zaika book, 7y.o."],
            ["What is a soul? - A soul is, when your mum puts some cookies for you on the table, and you leave them for your little brother.","Zaika book, 8y.o."], 
            ["What is a soul?  - The soul has the shape of a heart.","Zaika book, 8y.o."],
            ["What Is sadness? – Sadness is when someone Is very sad, he goes to a friend of his and drinks a lot.","Zaika book, 7y.o."],
            ["What is patience? – Patience means, when someone goes to the grocery store and has to wait in line.","Zaika book, 7 y.o."],
            ["Why do horses have horseshoes? - Horseshoes are put on the horse, because they are lighter than him and move faster.","Zaika book, 8y.o."],
            ["Why do horses have horseshoes? -Horseshoes are placed on the horse, so that he does not fall on his back. When the leash is pulled, he stops, thanks to the horseshoes.","Zaika book, 9y.o."],
            ["Why do horses have horseshoes? - Horseshoes are put on his horse to knock on the streets, because otherwise he would not be a horse.","Zaika book, 7 y.o."], 
            ["What is respect?  - Respect means getting up from the chair, for the grandmothers to sit on.","Zaika book, 9y.o."],
            ["What is freedom? – Freedom is when you’re allowed to have day off on Sunday.","Zaika book, 6y.o."],
            ["What is a country? – A country is a guy, who owns the police.","Zaika book, 7y.o."],
            ["What is a country?  - A country Is a guy, who says, what should be sold in the groceryshop.","Zaika book, 7y.o."],
            ["What does the word modern mean? – Modern is when you see something nice and expensive, but you don’t have the money for it.","Zaika book, 12y.o."],
            ["How do migratory birds manage to fly thousands of kilometers day and night?   - Swallows, when they leave for the warm countries, they settle on the stork's wings and rest. When they set out on such a long journey, the birds take food.","Zaika book, 7y.o."], 
            ["How do birds or animals understand each other, while we, humans can talk and sometimes do not understand each other? - Birds and animals gather and talk to each other in whispers, and to us they only say  'meow'.","Zaika book, 10y.o."],
            ["How do birds or animals understand each other, while we, humans can talk and sometimes do not understand each other? - Fish understand each other when they make bubbles with their mouths.","Zaika book, 8y.o."],
            ["How do birds or animals understand each other, while we, humans can talk and sometimes do not understand each other?  - Fish talk by signs. Their mother teaches them the alphabet of fins.","Zaika book, 8y.o."],
            ["How do people from TV know, what the weather the next day will be? – The man from TV knows that tomorrow will rain, because he reads, what his mama wrote to him.","Zaika book, 6y.o."],
            ["If Earth is spinning, why don’t we fall out? -  It’s only the Earth, that is spinning. The streets don’t.","Zaika book, 6y.o."],
            ["If Earth is spinning, why don’t we fall out?  - Earth has round shape. We don’t fall out, cause we don’t go, where it’s round.","Zaika book, 7y.o."], 
            ["Why is Earth spinning? -  The Earth is spinning, so all the world can have Earth. It, when spins, gives Earth to all sides.","Zaika book, 7y.o."],
            [" What is an eclipse?   - Eclipse is an absence.","Zaika book, 12y.o."],
            ["What is time?  - Time is time, that flows all the time.","Zaika book, 5y.o."],
            ["What is an ambition? – Ambition in life, means to be selfish","Zaika book, 10y.o."],
            ["What does a grown-up means? – A grown up means an old child.","Zaika book, 10y.o."],
            ["What is a skeleton? – The skeleton helps for the development of science.","Zaika book, 10y.o."], 
            ["What is top secret? - It is top secret when the police should not  know.","Zaika book, 6y.o."],
            ["What is a smile? -To smile means to laugh inside your mind.","Zaika book, 8y.o."],
            ["What is a smile? -  Smiling is when some people laugh with their mouths shut, so not to disturb others.","Zaika book, 7y.o."],
            ["Why do we wash with a soap? – We wash that way, to put soap in the eyes of the microbes.","Zaika book, 5y.o."],
            ["What are the tears? – The tears are made out of the sea, and that’s why they are salty.","Zaika book, 7y.o."],
            ["What are the tears?  - Tears appear when the brain thinks and sweats and sweat comes out through the eyes.","Zaika book, 11y.o."], 
            ["How many years does childhood last? - Children live 35 years, young people 25, and adults die in 5 years.","Zaika book, 8y.o."],
            ["How many years does childhood last? - Childhood lasts the longest and you want to grow up all the time.","Zaika book, 9y.o."],
            ["How many years does childhood last? - Childhood lasts 5 years and then comes school.","Zaika book, 6y.o."],
            ["What is a talant? -Talant is the beauty of the mind.","Zaika book, 12y.o."],
            ["What are the neighbors? - Neighbors are people who live in the same place and when you run out of flour, they borrow.","Zaika book, 7y.o."],
            ["What is fog? - Fog is smoke that goes to the sky, because there is no place here.","Zaika book, 7y.o."], 
            ["What is fog? - Fog is a dense light, through which we cannot see.","Zaika book, 9y.o."],
            ["What is fog? - Fog is light darkness.","Zaika book, 5y.o."],
            ["What is fog? – Fog is frozen wind.","Zaika book, 7y.o."],
            ["What is fog? – Fog are the skies, who has fallen down.","Zaika book, 7y.o."],
            ["What are microbes? - Microbes are very small beetles that hide. They see that you bought potatoes, they jump on them and if you don't wash them, you die.","Zaika book, 7y.o."],
            ["How do fireflies glow? - Fireflies have a little hair and gas and the dwarves give them fire to ignite. Fireflies do not die, they glow until the fire goes out and when more hair grows, they glow again.","Zaika book, 10y.o."], 
            ["How do fireflies glow? - Fireflies can glow because they are small pieces of a star. When a person dies, a star falls and fireflies are born from this star.","Zaika book, 10y.o."],
            ["How do fireflies glow?-Fireflies are tiny, they have a lamp and go to the people who dream, illuminate them with the lamp to see what they are dreaming.","Zaika book, 7y.o."],
            ["Why some snail do have a house, and others don’t? - Some snails have houses because they ate plaster.","Zaika book, 12y.o."],
            ["Why some snail do have a house, and others don’t?- Some snails have houses because they have been saving, they have not eaten potatoes, only flowers, and so over time they have built houses.","Zaika book, 7y.o."],
            ["Do you think stars and fireflies talk to each other during the night? - The stars ask the little fireflies what they do in their short lives, and the fireflies wonder what the stars eat, that they live so long.","Zaika book, 12y.o."],
            ["Why some spiders have a little cross on their back?  - Because, those are their priests.","Zaika book, 8y.o."],
            ["Why does the conductor wave  a wand when he conducts? – He waves a wand, to show the direction of the sound.","Zaika book, 11y.o."],
            ["Why does the conductor wave  a wand when he conducts?  - The conductor has a wand because it's ugly to point a finger at the bass player, to show him where the symphony is going.","Zaika book, 10y.o."],
            ["Why don't all people speak the same language? - If everyone spoke the language, the names of the streets would be confused and all people would go to the country, that is the best.","Zaika book, 7y.o."], 
            ["Why do we dream? -  Dreams are there,  so you can sleep. Because the eyes are constantly seeing something, they want to see something at night.","Zaika book, 7y.o."],
            ["Why do we dream? -  Dreams are about being able to see your father when he dies.","Zaika book, 7y.o."],
            ["Why do we dream? - We dream, so not to be bored at night.","Zaika book, 7y.o."],
            ["Why do flowers have a scent? - The flower smells, because when the bee comes and takes it honey, at least the aroma remains.","Zaika book, 8y.o."],
            ["Why doesn't the hen fly like the other birds?  - The hen does not fly as high as other birds because she is afraid of losing her egg.","Zaika book, 7y.o."],
            ["Why is milk white and not green like grass? - Milk is white because in winter, when there is no grass, the cow eats paper.","Zaika book, 7y.o."],
            ["Why does the blood move through the human body and does not stop? -  Blood moves through the body to catch germs and drown them.","Zaika book, 6y.o."],
            ["What color is the water? In water, there is a little of each color, and milk is only white.","Zaika book, 7y.o."],
            ["What color is the water?  - The water has a glass color.","Zaika book, 8y.o."], 
            ["What color is the water? -  The water has a shiny color.","Zaika book, 7y.o."],
            ["What are the eyebrows for?- The eyebrows are to keep the forehead high and not fall on the eyes.","Zaika book, 6y.o."],
            ["At the door of someone's heart should we pray, break in or knock?- At the door of someone's heart you should neither knock, nor invade, nor pray, but only sing.","Zaika book, 11y.o."],
            ["What language is spoken in Heaven and Hell?-  In Heaven and Hell no language is spoken, because everything has already been said before we get there.","Zaika book, 8y.o."],
            ["The reason I love kids so much is because they’re so honest, so you know right away if they like you or they don’t.","Colin Egglesfield"],
            ["I love kids, but they are a tough audience.","Robbin Williams"],
            ["Encourage don’t belittle, embrace their individuality. And show them that no matter what they will always have value if they stay true to themselves.","Solange Nicole"],
            ["Life affords no greater responsibility, no greater privilege, than the raising of the next generation.","C. Everett Koop"],
            ["If your child marches to a different beat, a different drummer, you might just have to go along with that music. Help them achieve what’s important to them.","Sonia Sotomayor"], 
            ["Educating the mind, without educating the heart, is no education at all.","Aristotle"],
            ["Every child has a different learning style and pace. Each child is unique, not only capable of learning, but also capable of succeeding.","Robert John Meehan"],
            ["To educate a child, is to turn walls itno doors.","Anonymous"],
            ["The word ‘education’ comes from the Latin ‘educere’ = e- (out of) + -ducere (to draw). Education is not just about putting information in. We have forgotten that it, in fact, begins in the child’s heart.","Vince Gowmon"],
            ["By education I mean an all-round drawing out of the best in the child and man; body, mind and spirit.","Mahatma Gandhi"],
            ["I really love being human. But some days I really wish I could be fairy.","Greta, age 4"],
            ["If children feel safe, they can take risks, ask questions, make mistakes, learn to trust, share their feelings, and grow.","Alfie Kohn"],
            ["Let the child be the scriptwriter, the director and the actor in his own play.","Magda Gerber"],
            ["Since the jobs that our preschoolers will do probably don’t exist yet, our priority is to teach them the skills to adapt and inquire and question and cooperate…life skills.","Caroline Bellouse"], 
            ["Our children should be properly introduced to the world in which they live.","Thomas Berry"],
            ["Too much leading and we create anxiety for children. Too much following and the same is true. In wisdom we find balance between the two.","Vince Gowmon"],
            ["No significant learning occurs without a significant relationship.","James Comer"],
            ["The moment I decided to follow instead of lead, I discovered the joys of becoming part of a small child’s world.","Janet Gonzalez-Mena"],
            ["The art of teaching is the art of assisting discovery.","Mark Van Doren"],
            ["The best teachers are those who show you where to look, but don’t tell you what to see.","Alexandra K. Trenfor"],
            ["If we want children to become creative leaders then we must learn to follow their lead at an early age.","Vince Gowmon"],
            ["Curiosity is the wick in the candle of learning.","William Arthur Ward"],
            ["Children are not the people of tomorrow, but people today. They are entitled to be taken seriously. They have a right to be treated by adults with tenderness and respect, as equals.","Janusz Korczak"],
            ["It is not the answer that enlightens, but the question.","Eugene Ionesco"],
            ["All too often we are giving young people cut flowers when we should be teaching them to grow their own plants.","J.W. Gardner"],
            ["Don’t educate a child to become something or someone, educate to help them explore and celebrate who they already are.","Vince Gowmon"],
            ["Children learn how to make good decisions by making decisions, not by following directions.","Alfie Kohn"],
            ["Children come into the world exquisitely designed, and strongly motivated, to educate themselves. They don’t need to be forced to learn.","Peter Gray"],
            ["Truly wonderful, the mind of a child is.","Yoda"],
            ["The real magic wand is the child’s own mind.","Jose Ortega y Gasset"],
            ["Teach children what to think and you limit them to your ideas. Teach children how to think and their ideas are unlimited.","Sandra Parks"],
            ["Are we forming children who are only capable of learning what is known, or should we try to develop creative and innovative minds?","Jean Piaget"],
            ["The true sign of intelligence is not knowledge but imagination.","Albert Einstein"],
            ["Stop trying to turn children into someone they are not. Instead, let them unfold into who no human can imagine them to be.","Vince Gowmon"],
            ["Your image of the child is where teaching begins.","Loris Malaguzzi"],
            ["When one teaches, two learn.","Robert Heinlein"],
	    ]

    def get_quote(self):
        quote = random.choice(self.list)
        return quote