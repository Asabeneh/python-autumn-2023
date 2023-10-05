def find_word_variety(txt):
    lowered_case_text = txt.lower()
    cleaned_text = txt.replace('.', '').replace('’', '').replace(',',' ').replace('-', '').replace('_','').replace('–', '')
    words = cleaned_text.split()
    unique_words = set(words)
    total_number_words = len(words)
    total_number_unique_words = len(unique_words)
    word_variety = total_number_unique_words / total_number_words * 100
    return [total_number_words,  total_number_unique_words, word_variety]

obama_txt = '''
My fellow citizens:I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.
Forty-four Americans have now taken the presidential oath. The words have been spoken during rising tides of prosperity and the still waters of peace. Yet, every so often the oath is taken amidst gathering clouds and raging storms. At these moments, America has carried on not simply because of the skill or vision of those in high office, but because We the People have remained faithful to the ideals of our forbearers, and true to our founding documents.
So it has been. So it must be with this generation of Americans.

That we are in the midst of crisis is now well understood. Our nation is at war, against a far-reaching network of violence and hatred. Our economy is badly weakened, a consequence of greed and irresponsibility on the part of some, but also our collective failure to make hard choices and prepare the nation for a new age. Homes have been lost; jobs shed; businesses shuttered. Our health care is too costly; our schools fail too many; and each day brings further evidence that the ways we use energy strengthen our adversaries and threaten our planet.

These are the indicators of crisis, subject to data and statistics. Less measurable but no less profound is a sapping of confidence across our land - a nagging fear that America's decline is inevitable, and that the next generation must lower its sights.

Today I say to you that the challenges we face are real. They are serious and they are many.

They will not be met easily or in a short span of time. But know this, America - they will be met. On this day, we gather because we have chosen hope over fear, unity of purpose over conflict and discord.

On this day, we come to proclaim an end to the petty grievances and false promises, the recriminations and worn out dogmas, that for far too long have strangled our politics.

We remain a young nation, but in the words of Scripture, the time has come to set aside childish things. The time has come to reaffirm our enduring spirit; to choose our better history; to carry forward that precious gift, that noble idea, passed on from generation to generation: the God-given promise that all are equal, all are free, and all deserve a chance to pursue their full measure of happiness.

In reaffirming the greatness of our nation, we understand that greatness is never a given. It must be earned. Our journey has never been one of short-cuts or settling for less. It has not been the path for the faint-hearted - for those who prefer leisure over work, or seek only the pleasures of riches and fame. Rather, it has been the risk-takers, the doers, the makers of things - some celebrated but more often men and women obscure in their labor, who have carried us up the long, rugged path towards prosperity and freedom.

For us, they packed up their few worldly possessions and traveled across oceans in search of a new life.

For us, they toiled in sweatshops and settled the West; endured the lash of the whip and plowed the hard earth.
For us, they fought and died, in places like Concord and Gettysburg; Normandy and Khe Sahn. Time and again these men and women struggled and sacrificed and worked till their hands were raw so that we might live a better life. They saw America as bigger than the sum of our individual ambitions; greater than all the differences of birth or wealth or faction.

This is the journey we continue today. We remain the most prosperous, powerful nation on Earth. Our workers are no less productive than when this crisis began. Our minds are no less inventive, our goods and services no less needed than they were last week or last month or last year. Our capacity remains undiminished. But our time of standing pat, of protecting narrow interests and putting off unpleasant decisions - that time has surely passed. Starting today, we must pick ourselves up, dust ourselves off, and begin again the work of remaking America.

For everywhere we look, there is work to be done. The state of the economy calls for action, bold and swift, and we will act - not only to create new jobs, but to lay a new foundation for growth. We will build the roads and bridges, the electric grids and digital lines that feed our commerce and bind us together. We will restore science to its rightful place, and wield technology's wonders to raise health care's quality and lower its cost. We will harness the sun and the winds and the soil to fuel our cars and run our factories. And we will transform our schools and colleges and universities to meet the demands of a new age. All this we can do. And all this we will do.

Now, there are some who question the scale of our ambitions - who suggest that our system cannot tolerate too many big plans. Their memories are short. For they have forgotten what this country has already done; what free men and women can achieve when imagination is joined to common purpose, and necessity to courage.

What the cynics fail to understand is that the ground has shifted beneath them - that the stale political arguments that have consumed us for so long no longer apply. The question we ask today is not whether our government is too big or too small, but whether it works - whether it helps families find jobs at a decent wage, care they can afford, a retirement that is dignified. Where the answer is yes, we intend to move forward. Where the answer is no, programs will end. And those of us who manage the public's dollars will be held to account - to spend wisely, reform bad habits, and do our business in the light of day - because only then can we restore the vital trust between a people and their government.

Nor is the question before us whether the market is a force for good or ill. Its power to generate wealth and expand freedom is unmatched, but this crisis has reminded us that without a watchful eye, the market can spin out of control - and that a nation cannot prosper long when it favors only the prosperous. The success of our economy has always depended not just on the size of our Gross Domestic Product, but on the reach of our prosperity; on our ability to extend opportunity to every willing heart - not out of charity, but because it is the surest route to our common good.

As for our common defense, we reject as false the choice between our safety and our ideals. Our Founding Fathers, faced with perils we can scarcely imagine, drafted a charter to assure the rule of law and the rights of man, a charter expanded by the blood of generations. Those ideals still light the world, and we will not give them up for expedience's sake. And so to all other peoples and governments who are watching today, from the grandest capitals to the small village where my father was born: know that America is a friend of each nation and every man, woman, and child who seeks a future of peace and dignity, and that we are ready to lead once more.

Recall that earlier generations faced down fascism and communism not just with missiles and tanks, but with sturdy alliances and enduring convictions. They understood that our power alone cannot protect us, nor does it entitle us to do as we please. Instead, they knew that our power grows through its prudent use; our security emanates from the justness of our cause, the force of our example, the tempering qualities of humility and restraint.

We are the keepers of this legacy. Guided by these principles once more, we can meet those new threats that demand even greater effort - even greater cooperation and understanding between nations. We will begin to responsibly leave Iraq to its people, and forge a hard-earned peace in Afghanistan. With old friends and former foes, we will work tirelessly to lessen the nuclear threat, and roll back the specter of a warming planet. We will not apologize for our way of life, nor will we waver in its defense, and for those who seek to advance their aims by inducing terror and slaughtering innocents, we say to you now that our spirit is stronger and cannot be broken; you cannot outlast us, and we will defeat you.

For we know that our patchwork heritage is a strength, not a weakness. We are a nation of Christians and Muslims, Jews and Hindus - and non-believers. We are shaped by every language and culture, drawn from every end of this Earth; and because we have tasted the bitter swill of civil war and segregation, and emerged from that dark chapter stronger and more united, we cannot help but believe that the old hatreds shall someday pass; that the lines of tribe shall soon dissolve; that as the world grows smaller, our common humanity shall reveal itself; and that America must play its role in ushering in a new era of peace.

To the Muslim world, we seek a new way forward, based on mutual interest and mutual respect.

To those leaders around the globe who seek to sow conflict, or blame their society's ills on the West - know that your people will judge you on what you can build, not what you destroy. To those who cling to power through corruption and deceit and the silencing of dissent, know that you are on the wrong side of history; but that we will extend a hand if you are willing to unclench your fist.

To the people of poor nations, we pledge to work alongside you to make your farms flourish and let clean waters flow; to nourish starved bodies and feed hungry minds. And to those nations like ours that enjoy relative plenty, we say we can no longer afford indifference to suffering outside our borders; nor can we consume the world's resources without regard to effect. For the world has changed, and we must change with it.

As we consider the road that unfolds before us, we remember with humble gratitude those brave Americans who, at this very hour, patrol far-off deserts and distant mountains. They have something to tell us today, just as the fallen heroes who lie in Arlington whisper through the ages.

'''
donald_speech= '''
Chief Justice Roberts, President Carter, President Clinton,President Bush, fellow Americans and people of the world – thank you.
 We the citizens of America have now joined a great national effort to rebuild our county and restore its promise for all our people.
Together we will determine the course of America for many, many years to come.
Together we will face challenges. We will confront hardships. But we will get the job done.
Every four years we gather on these steps to carry out the orderly and peaceful transfer of power.
And we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent, thank you.
Today’s ceremony, however, has very special meaning because today we are not merely transferring power from one administration to another – but transferring it from Washington DC and giving it back to you the people.
For too long a small group in our nation’s capital has reaped the rewards of government while the people have borne the cost.
Washington flourished but the people did not share in its wealth. Politicians prospered but the jobs left and the factories closed.The establishment protected itself but not the citizens of our country.
Their victories have not been your victories. Their triumphs have not been your triumphs. While they have celebrated there has been little to celebrate for struggling families all across our land.
That all changes starting right here and right now because this moment is your moment. It belongs to you. It belongs to everyone gathered here today and everyone watching all across America today.
This is your day.This is your celebration.And this – the United States of America – is your country.What truly matters is not what party controls our government but that this government is controlled by the people.
Today, January 20 2017, will be remembered as the day the people became the rulers of this nation again.The forgotten men and women of our country will be forgotten no longer. Everyone is listening to you now.
You came by the tens of millions to become part of a historic movement –  the likes of which the world has never seen before.
At the centre of this movement is a crucial conviction – that a nation exists to serve its citizens.Americans want great schools for their children, safe neighbourhoods for their families and good jobs for themselves.
These are just and reasonable demands.Mothers and children trapped in poverty in our inner cities, rusted out factories scattered like tombstones across the landscape of our nation.
An education system flushed with cash, but which leaves our young and beautiful students deprived of all knowledge. And the crime and the gangs and the drugs which deprive people of so much unrealised potential.
We are one nation, and their pain is our pain, their dreams are our dreams, we share one nation, one home and one glorious destiny.
Today I take an oath of allegiance to all Americans. For many decades, we’ve enriched foreign industry at the expense of American industry, subsidised the armies of other countries, while allowing the sad depletion of our own military.
We've defended other nations’ borders while refusing to defend our own.And spent trillions and trillions of dollars overseas while America’s infrastructure has fallen into disrepair and decay.
We have made other countries rich while the wealth, strength and confidence of our country has dissipated over the horizon.
One by one, shutters have closed on our factories without even a thought about the millions and millions of those who have been left behind.
But that is the past and now we are looking only to the future.
We assembled here today are issuing a new decree to be heard in every city, in every foreign capital, in every hall of power – from this day on a new vision will govern our land – from this day onwards it is only going to be America first – America first!
Every decision on trade, on taxes, on immigration, on foreign affairs will be made to benefit American workers and American families.
Protection will lead to great prosperity and strength. I will fight for you with every bone in my body and I will never ever let you down.
America will start winning again. America will start winning like never before.
We will bring back our jobs, we will bring back our borders, we will bring back our wealth, we will bring back our dreams.
We will bring new roads and high roads and bridges and tunnels and railways all across our wonderful nation.
We will get our people off welfare and back to work – rebuilding our country with American hands and American labour.
We will follow two simple rules – buy American and hire American.
We see good will with the nations of the world but we do so with the understanding that it is the right of all nations to put their nations first.
We will shine for everyone to follow.We will reinforce old alliances and form new ones, and untie the world against radical Islamic terrorism which we will eradicate from the face of the earth.
At the bed rock of our politics will be an allegiance to the United States.And we will discover new allegiance to each other. There is no room for prejudice.
The bible tells us how good and pleasant it is when god’s people live together in unity.When America is united, America is totally unstoppable
There is no fear, we are protected and will always be protected by the great men and women of our military and most importantly we will be protected by god.
Finally, we must think big and dream even bigger. As Americans, we know we live as a nation only when it is striving.
We will no longer accept politicians who are always complaining but never doing anything about it.The time for empty talk is over, now arrives the hour of action.
Do not allow anyone to tell you it cannot be done. No challenge can match the heart and fight and spirit of America. We will not fail, our country will thrive and prosper again.
We stand at the birth of a new millennium, ready to unlock the mysteries of space, to free the earth from the miseries of disease, to harvest the energies, industries and technologies of tomorrow.
A new national pride will stir ourselves, lift our sights and heal our divisions. It’s time to remember that old wisdom our soldiers will never forget, that whether we are black or brown or white, we all bleed the same red blood of patriots.
We all enjoy the same glorious freedoms and we all salute the same great American flag and whether a child is born in the urban sprawl of Detroit or the windswept plains of Nebraska, they look at the same night sky, and dream the same dreams, and they are infused with the breath by the same almighty creator.
So to all Americans in every city near and far, small and large, from mountain to mountain, from ocean to ocean – hear these words – you will never be ignored again.
Your voice, your hopes and dreams will define your American destiny.Your courage, goodness and love will forever guide us along the way.
Together we will make America strong again, we will make America wealthy again, we will make America safe again and yes – together we will make America great again.
Thank you.
God bless you.
And god bless America.
'''
print(find_word_variety(obama_txt))
print(find_word_variety(donald_speech))
