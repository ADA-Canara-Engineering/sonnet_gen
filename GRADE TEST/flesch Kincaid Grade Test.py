# Readability test --  Flesch Kincaid Grade Level

#here are the 10 randomanly generated sonnet from the created model, 
#Flesch Kincaid Grade Level test is done on these generated sonnets and 
#the result of 43.28 is obtained which best suits the property of sonnet.


from readability import Readability

text = ''' be may the love , for the soul compare 
 in rest pride , when the bland of worth 
 and in the soul of the flowers and shade 
 and love 's soul and like , and the soul and store 
 and far it , i die like thy shall stold 
 the whose like the blood and her black 
 and speed with was love , which bare the world 
 and the strong the dreast of her hold we light 
 whose charms thy gartion of round and cold 
 the with a mind , and shall encerest the skeel 
 the fare of your heart of more the fair 
 of man whose seems that god in thy bright 
 which companced to the bless dark , and she 
 that doth which had thou thought.

why soul , and when the strang sure 
 have sate the worn at soul and have seen 
 not so i far in the flict her sweet 
 thou whose that of the streake , and not the heart 
 and such and before despitor of my brow 
 but be the which are beaute upon the green 
 but all of this with one the have despise 
 and the was a flowers and such love 
 and with a lies to in the which be 
 the shiply known , that i have stone of love 
 so that i die batters , not of her stars 
 the stars and thou , the words he soul 
 which heart to her heart , and the intend 
 who was like the sun of the step with song.


of my livine , and are and like the stare 
 faint and the warrang , and have then death 
 but thought straight had the sense and say 
 and shine all my things all of the strange 
 have heart of state , and sound of should 
 hat seem to unfell 'd to change to men 
 the pain 'd her beauty , and of death 
 when a stars and such left of the earth 
 the rove is the stolich of the string 
 but the world , i strained , and , in the love 
 and the streams while from the soul it well 
 that lation as a limber 'd streake 
 our fatit , and in her forread dear 
 and perest of that life , who with men thee .


for all mankind , nor for it dies in the light 
 the more the vigetn , and and heart , and state 
 shine the chare could , miss it , who sabe 
 the soul and thy flame the limber strength 
 and point mide through the rest de might 
 and the make at it shall the thought of men 
 his falle of the world be not of the speat 
 whose sweet his for the rest remell 'd 
 and whose vain 'd the more consted land 
 the still the work of things of your from 
 his wound the strange of the fate of the that 
 and from the fight to the from the strange 
 the still 's come not than are with little stars 
 and hour thoughts unto the soul made. 



 i look 's will to love the flict of love 
 but so man , and the storm , and man the shole 
 when she more and for the should the pare 
 and to see , and the soul and seems of stream 
 and mount the parts , and the strook 's spring 
 the work and land , and the with this man 
 and with once and the pain , and all the blow 
 and little spot he heart him with the see 
 that wander thing the smole of the strife 
 and when still behold the fleeding be the strange 
 so sole then a long of the shack dedied 
 so this not we cassed to one all her dead 
 the world like be was a set when the dust 
 when her to the world batters.


and the night pass , and the strange say 
 that sings with sland in the black stall 
 the war his fair bear i 's sake to see 
 her trees , and in the seem 'd the laid 
 the world couns , that in the with the world 
 and his as all the string still they shall smile 
 and hour of the wait , but whose life 's stees 
 and wast with very with like the strong 
 and stream and heart , and not the flee 
 and charge , no summer , all while of the last 
 obed strong , all father man of thought 
 of vilace thing the brow the post beauty 
 the strayed heaven son , and the poor blood 
 and that more the soul and the called the strange .

swifter than the rate of the was commere 
 in the strange beturn are mount be the world
 then for the free , and bower of her faith 
 the world mute and face , thy shall was the down 
 the world we sear , and to her gods was oun 
 the while of the cloud 'd as the streaves 
 the strong and light , and when the strange 
 that this where the ware , and the wall 
 for thou methought full , and , in desing 
 the shall on a look were not the storn 
 the song of the string and the strove 
 the breath all the light in my shill wheee 
 and stall the storm 'd hope , for the fair 
 while the sun of some body , the white .


that shall behold not so abhorred the hour 
 so might so shall which heaven to the strong 
 of the world fath me , yet through the fair 
 and in the broken stream , of worth set the grace
 the last spoul , but not the ungret that 
 and strange the lates , and stall , and in the streast 
 to sweet might , and her , all the burn 
 and from the through a form to god 
 and seen the played of lack and to the look 
 and was i mount the find with the world 
 and race and loath cith sound , and the grain 
 whose man the strange of the was he stood 
 and for the last , and thy the most of a care 
 and of the stronger 's love you to the crees .


to lay thee out upon the couch , and make 
 the wonder plain , and i blang and rear 
 and strange the love of all the war the stream 
 when the goddest from the shill belied 
 for heart of starchous and his warrall 
 and lack the must of the strange of love 
 the shall pare , the far should was every 
 where the world spoke the storn she parts 
 who faither paunts parture let the last of streams 
 and art his was a wings of love and dead 
 for strength and men world of the pressing 
 love god the scorn , and will with the store 
 and sleep , while chose with stare while our change 
 and the long which strand , for the glorious bear.'''

r = Readability(text)
fk = r.flesch_kincaid()
fkk = r.flesch()



print("Score:  "fk.score)
print("Grade Level:  "fk.grade_level)


#30-50	score ensures  :
#difficult to read, best understood by college graduates
#so this ensures sonnet readebality.
#(source: https://yoast.com/flesch-reading-ease-score/ )