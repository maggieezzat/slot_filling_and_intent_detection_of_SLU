from googletrans import Translator
import os

def translate_slots(root_dir='/home/maggie/slot_filling_and_intent_detection_of_SLU/data/atis-2/'):
    
    file_en = root_dir + "vocab.slot"
    file_de = root_dir + "vocab_slot_de.txt"
    translator = Translator()
    with open(file_en, 'r') as f:
        with open(file_de, 'a') as out_f:
            
            #while True :
            line = f.readline()
            #if not line:
            #    break
            line = 'B-arrive_date.date_relative'
            letter = line.split('-')[0].strip()
            label = line.split('-')[1].strip()
            text=[]
            if '.' in label:
                label_1 = label.split('.')[0]
                label_2 = label.split('.')[1]
                labels_1 = label_1.split('_')
                labels_2 = label_2.split('_')

                for l in labels_1:
                    print(l)
                    text.append(translator.translate(l, src='en', dest='de').text.lower())
                for l in labels_2:
                    print(l)
                    text.append(translator.translate(l, src='en', dest='de').text.lower())
            else:
                labels = label.split('_')
                for l in labels:
                    text.append(translator.translate(l, src='en', dest='de').text.lower())
                
            print(text)
            #line = line.split('<=>')
            #sent = line[0].strip()
            #words_labels = sent.split(' ')
            #words = [word_label.split(':')[0] for word_label in words_labels ]
            #labels = [word_label.split(':')[1] for word_label in words_labels ] 
            #intent = line[1].strip()

            #trans = ""
            #for i in range(len(words)):
            #    text = translator.translate(words[i], src='en', dest='de').text.lower()
            #    trans+= text+":"+labels[i] + " "
            #trans+= "<=> " + intent
            #out_f.write(trans + "\n")


    #B-airport_code
    #B-airport_name
    #B-arrive_date.date_relative
    #B-arrive_date.day_name
    #B-arrive_date.day_number

def translate_data(file, root_dir='/home/maggie/slot_filling_and_intent_detection_of_SLU/data/atis-2/'):

    file_en = root_dir + file
    file_de = root_dir + file + "_de.txt"
    #translator = Translator()
    with open(file_en, 'r') as f:
        with open(file_de, 'a') as out_f:
            i=0
            while True :
                line = f.readline()
                if not line:
                    break
                
                line = line.split('<=>')
                sent = line[0].strip()
                words_labels = sent.split(' ')
                words = [word_label.split(':')[0] for word_label in words_labels ]
                labels = [word_label.split(':')[1] for word_label in words_labels ] 
                intent = line[1].strip()

                trans = ""
                for i in range(len(words)):
                    translator = Translator()
                    try:
                        
                        text = translator.translate(words[i], src='en', dest='de').text.lower()
                        trans+= text+":"+labels[i] + " "
                        i+=1
                        print(str(i))
                    except Exception as e:
                        print(str(e))
                        continue
                        #print("error", end='\r')
                trans+= "<=> " + intent
                out_f.write(trans + "\n")


        

def main():
    translate_data("test")
    translate_data("valid")
    translate_data("train")
    translate_slots()

if __name__ == "__main__":
    main()