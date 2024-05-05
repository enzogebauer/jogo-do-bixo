import xmlrpc.server

class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question_text": "Qual destes não é considerado uma hortaliça?", 
                "options": ["Cenoura", "Batata", "Maçã", "Alface"],
                "correct_option": "Maçã"
            },
            {
                "question_text": "Qual destas hortaliças é conhecida por ser uma excelente fonte de vitamina C?", 
                "options": ["Brócolis", "Cebola", "Abóbora", "Pimentão"],
                "correct_option": "Abóbora"
            },
            {
                "question_text": "Qual é a parte da planta que normalmente comemos nas cenouras?", 
                "options": ["Raiz", "Folhas", "Caule", "Fruto"],
                "correct_option": "Raiz"
            },
            {
                "question_text": "Qual destas hortaliças é conhecida por ser rica em ferro?", 
                "options": ["Alface", "Espinafre", "Pepino", "Tomate"],
                "correct_option": "Espinafre"
            },
            {
                "question_text": "Qual destas hortaliças é geralmente consumida como uma leguminosa?", 
                "options": ["Ervilha", "Rúcula", "Alho-poró", "Beterraba"],
                "correct_option": "Ervilha"
            },
            {
                "question_text": "Qual destas hortaliças é considerada uma excelente fonte de fibras?", 
                "options": ["Pepino", "Abóbora", "Couve-flor", "Feijão"],
                "correct_option": "Abóbora"
            }
        ]

        self.total_points = 0

    def get_list(self):
        if self.questions:
            return self.questions
        else:
            return "finished"

    def check_answer(self, question_text, answer):
        for question in self.questions:
            if question["question_text"] == question_text:
                if question["correct_option"] == answer:
                    self.total_points += 1
                self.questions.remove(question)
                return

    def get_total_points(self):
        return self.total_points

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_instance(Quiz())
server.serve_forever()
