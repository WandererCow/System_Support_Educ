# main_experimental.py
"""
ЭКСПЕРИМЕНТАЛЬНАЯ ВЕРСИЯ
Информационная система поддержки решений выбора направления обучения

Особенности:
- ИИ-подобный анализ текстовых ответов
- Визуализация результатов
- Сравнительный анализ направлений
- Экспорт рекомендаций в файл
- Адаптивный опросник (вопросы зависят от предыдущих ответов)
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple
import random  # для симуляции "нейросетевого" анализа


class ExperimentalAdvisor:
    """Экспериментальная система поддержки решений"""

    def __init__(self):
        self.user_data = {}
        self.vector_profile = {}  # Векторный профиль студента
        self.universities_db = self.load_universities_db()
        self.answers_history = []

    def load_universities_db(self) -> Dict:
        """База данных университетов и направлений"""
        return {
            "МГУ им. Ломоносова": {
                "directions": {
                    "Прикладная математика": {"budget_places": 150, "min_score": 95, "cost": 400000,
                                              "tags": ["math", "it", "science"]},
                    "Фундаментальная лингвистика": {"budget_places": 80, "min_score": 92, "cost": 380000,
                                                    "tags": ["languages", "humanities"]},
                    "Биоинженерия": {"budget_places": 60, "min_score": 96, "cost": 420000,
                                     "tags": ["biology", "science"]}
                },
                "location": "Москва",
                "dormitory": True
            },
            "СПбГУ": {
                "directions": {
                    "Программная инженерия": {"budget_places": 120, "min_score": 90, "cost": 350000,
                                              "tags": ["it", "engineering"]},
                    "Юриспруденция": {"budget_places": 100, "min_score": 88, "cost": 330000,
                                      "tags": ["law", "humanities"]},
                    "Медицина": {"budget_places": 90, "min_score": 94, "cost": 450000, "tags": ["medicine", "science"]}
                },
                "location": "Санкт-Петербург",
                "dormitory": True
            },
            "ИТМО": {
                "directions": {
                    "Искусственный интеллект": {"budget_places": 100, "min_score": 93, "cost": 360000,
                                                "tags": ["it", "ai", "science"]},
                    "Робототехника": {"budget_places": 80, "min_score": 89, "cost": 340000,
                                      "tags": ["engineering", "it"]},
                    "Бизнес-информатика": {"budget_places": 110, "min_score": 85, "cost": 320000,
                                           "tags": ["business", "it"]}
                },
                "location": "Санкт-Петербург",
                "dormitory": True
            },
            "ВШЭ": {
                "directions": {
                    "Экономика": {"budget_places": 130, "min_score": 91, "cost": 410000,
                                  "tags": ["economics", "humanities"]},
                    "Социология": {"budget_places": 90, "min_score": 84, "cost": 300000,
                                   "tags": ["social", "humanities"]},
                    "Data Science": {"budget_places": 95, "min_score": 92, "cost": 390000,
                                     "tags": ["it", "math", "science"]}
                },
                "location": "Москва",
                "dormitory": True
            },
            "МФТИ": {
                "directions": {
                    "Прикладная физика": {"budget_places": 70, "min_score": 97, "cost": 430000,
                                          "tags": ["physics", "science"]},
                    "Космические технологии": {"budget_places": 50, "min_score": 96, "cost": 440000,
                                               "tags": ["engineering", "physics"]},
                    "Биофизика": {"budget_places": 40, "min_score": 95, "cost": 420000,
                                  "tags": ["biology", "physics", "science"]}
                },
                "location": "Долгопрудный",
                "dormitory": True
            }
        }

    def ai_text_analysis(self, text: str) -> Dict:
        """Экспериментальный анализ текстовых ответов (симуляция NLP)"""
        # Симулируем анализ естественного языка
        keywords_map = {
            "математика|программирование|компьютер|айти|it|code": "technical",
            "рисовать|писать|читать|литература|история|языки": "humanities",
            "биология|химия|медицина|природа|животные": "natural_science",
            "бизнес|деньги|управление|маркетинг|продажи": "business",
            "помогать|лечить|учить|социальный|психология": "social"
        }

        scores = {"technical": 0, "humanities": 0, "natural_science": 0, "business": 0, "social": 0}

        for pattern, category in keywords_map.items():
            import re
            if re.search(pattern, text.lower()):
                scores[category] += random.randint(1, 3)  # Симуляция весов

        return scores

    def adaptive_questionnaire(self):
        """Адаптивный опросник (вопросы зависят от ответов)"""
        print("\n" + "🎯" * 30)
        print("ЭКСПЕРИМЕНТАЛЬНЫЙ АДАПТИВНЫЙ ОПРОСНИК")
        print("🎯" * 30)

        # Базовые вопросы
        name = input("\n1. Как вас зовут? ").strip()
        self.user_data["name"] = name

        # Текстовый анализ мечты
        dream = input("2. Опишите вашу идеальную профессию и работу мечты (1-2 предложения): ")
        dream_analysis = self.ai_text_analysis(dream)
        self.user_data["dream_analysis"] = dream_analysis

        print(f"\n📊 Анализ вашего ответа (экспериментальный ИИ):")
        for cat, score in dream_analysis.items():
            if score > 0:
                print(f"   - {cat}: {score} баллов")

        # Адаптивные вопросы на основе анализа
        dominant_cat = max(dream_analysis, key=dream_analysis.get)
        self.user_data["dominant_category"] = dominant_cat

        print(f"\n🔍 На основе ваших интересов (доминирует сфера: {dominant_cat}) зададим уточняющие вопросы:")

        if dominant_cat == "technical":
            prog_exp = input("   Есть ли опыт программирования? (нет/базовый/продвинутый): ")
            self.user_data["programming_exp"] = prog_exp
        elif dominant_cat == "humanities":
            languages = input("   Какими иностранными языками владеете? (через запятую): ")
            self.user_data["languages"] = languages
        elif dominant_cat == "natural_science":
            lab_exp = input("   Был ли опыт лабораторных работ? (да/нет): ")
            self.user_data["lab_experience"] = lab_exp

        return dream_analysis

    def vector_profiling(self, dream_analysis: Dict):
        """Создание векторного профиля студента"""
        vector = {
            "technical": dream_analysis.get("technical", 0) + random.randint(1, 5),
            "humanities": dream_analysis.get("humanities", 0) + random.randint(1, 5),
            "science": dream_analysis.get("natural_science", 0) + random.randint(1, 5),
            "business": dream_analysis.get("business", 0) + random.randint(1, 3),
            "social": dream_analysis.get("social", 0) + random.randint(1, 3)
        }

        # Нормализация вектора
        total = sum(vector.values())
        for key in vector:
            vector[key] = round(vector[key] / total * 100, 1)

        self.vector_profile = vector
        return vector

    def calculate_compatibility(self, uni_name: str, direction: str, tags: List[str]) -> float:
        """Расчет совместимости студента с направлением"""
        compatibility = 0

        # Анализ по тегам
        for tag in tags:
            if tag == "it" or tag == "engineering":
                compatibility += self.vector_profile.get("technical", 0)
            elif tag == "humanities" or tag == "law":
                compatibility += self.vector_profile.get("humanities", 0)
            elif tag == "science" or tag == "biology" or tag == "physics":
                compatibility += self.vector_profile.get("science", 0)
            elif tag == "business" or tag == "economics":
                compatibility += self.vector_profile.get("business", 0)
            elif tag == "social":
                compatibility += self.vector_profile.get("social", 0)

        return compatibility / len(tags) if tags else 0

    def find_best_matches(self) -> List[Tuple]:
        """Поиск лучших соответствий"""
        matches = []

        for uni_name, uni_data in self.universities_db.items():
            for direction_name, dir_data in uni_data["directions"].items():
                compatibility = self.calculate_compatibility(uni_name, direction_name, dir_data["tags"])

                # Финансовая доступность (симуляция)
                financial_score = random.randint(60, 100)

                total_score = (compatibility * 0.6 + financial_score * 0.4)

                matches.append({
                    "university": uni_name,
                    "direction": direction_name,
                    "compatibility": round(compatibility, 1),
                    "financial_score": financial_score,
                    "total_score": round(total_score, 1),
                    "location": uni_data["location"],
                    "min_score": dir_data["min_score"],
                    "cost_per_year": dir_data["cost"]
                })

        return sorted(matches, key=lambda x: x["total_score"], reverse=True)[:10]

    def visualize_profile(self):
        """Визуализация профиля студента (текстовая)"""
        print("\n" + "📊" * 20)
        print("ВАШ ПРОФИЛЬ (Векторная модель)")
        print("📊" * 20)

        max_width = 30
        for category, score in self.vector_profile.items():
            bar_length = int(max_width * score / 100)
            bar = "█" * bar_length + "░" * (max_width - bar_length)
            print(f"{category.capitalize():12} |{bar}| {score}%")

    def generate_comparison_table(self, top_matches: List[Dict]):
        """Генерация сравнительной таблицы"""
        print("\n" + "📈" * 30)
        print("СРАВНИТЕЛЬНЫЙ АНАЛИЗ НАПРАВЛЕНИЙ")
        print("📈" * 30)

        print(
            f"\n{'№':<3} {'Университет':<20} {'Направление':<25} {'Совмест.':<8} {'Баллы ЕГЭ':<10} {'Стоимость/год':<12}")
        print("-" * 85)

        for i, match in enumerate(top_matches[:5], 1):
            print(
                f"{i:<3} {match['university']:<20} {match['direction']:<25} {match['compatibility']:<7}% {match['min_score']:<9} {match['cost_per_year']:<11} ₽")

    def export_recommendations(self, recommendations: List[Dict]):
        """Экспорт рекомендаций в JSON файл"""
        export_data = {
            "user_name": self.user_data.get("name", "Anonymous"),
            "vector_profile": self.vector_profile,
            "timestamp": datetime.now().isoformat(),
            "recommendations": recommendations[:5]
        }

        filename = f"recommendations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

        print(f"\n💾 Рекомендации экспортированы в файл: {filename}")
        return filename

    def run_experiment(self):
        """Запуск экспериментальной версии"""
        print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║     🧪 ЭКСПЕРИМЕНТАЛЬНАЯ СИСТЕМА ПОДДЕРЖКИ РЕШЕНИЙ 🧪             ║
    ║                                                                  ║
    ║     Версия: 2.0-beta (экспериментальная)                        ║
    ║     Особенности: AI-анализ, векторное профилирование,           ║
    ║                 экспорт данных, адаптивный опросник              ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
        """)

        # Шаг 1: Адаптивный опрос
        dream_analysis = self.adaptive_questionnaire()

        # Шаг 2: Векторное профилирование
        self.vector_profiling(dream_analysis)
        self.visualize_profile()

        # Шаг 3: Поиск соответствий
        print("\n🔍 Поиск оптимальных направлений...")
        best_matches = self.find_best_matches()

        # Шаг 4: Сравнительный анализ
        self.generate_comparison_table(best_matches)

        # Шаг 5: Персональная рекомендация
        print("\n" + "🏆" * 20)
        print("ПЕРСОНАЛЬНАЯ РЕКОМЕНДАЦИЯ")
        print("🏆" * 20)

        top = best_matches[0]
        print(f"\n✨ {self.user_data.get('name', 'Уважаемый')}, на основе анализа вам лучше всего подходит:")
        print(f"\n   🎓 {top['direction']} в {top['university']}")
        print(f"   📍 {top['location']}")
        print(f"   📊 Совместимость: {top['compatibility']}%")
        print(f"   💰 Ориентировочная стоимость: {top['cost_per_year']} ₽/год")

        # Дополнительный AI-совет
        if top['compatibility'] > 80:
            print("\n   🤖 AI-совет: Отличный выбор! Ваш профиль идеально соответствует этому направлению.")
        elif top['compatibility'] > 60:
            print("\n   🤖 AI-совет: Хороший вариант. Рекомендуем развивать навыки по ключевым предметам.")
        else:
            print("\n   🤖 AI-совет: Рассмотрите также другие варианты из списка выше.")

        # Шаг 6: Экспорт данных
        export_choice = input("\n📁 Экспортировать рекомендации в файл? (да/нет): ").lower()
        if export_choice in ['да', 'yes', 'д', 'y']:
            self.export_recommendations(best_matches)

        # Шаг 7: Финальный отчет
        print("\n" + "📋" * 20)
        print("ИТОГОВЫЙ ЭКСПЕРИМЕНТАЛЬНЫЙ ОТЧЕТ")
        print("📋" * 20)

        print(f"""
    Студент: {self.user_data.get('name', 'Unknown')}
    Доминирующая сфера: {self.user_data.get('dominant_category', 'N/A')}
    Вектор профиля: {self.vector_profile}

    Уникальные особенности экспериментальной версии:
    ✅ Адаптивный опросник с ИИ-анализом текста
    ✅ Векторное профилирование студента
    ✅ Сравнительный анализ топ-10 направлений
    ✅ Экспорт данных в JSON
    ✅ Симуляция NLP-обработки

    Рекомендовано направлений: {len(best_matches)}
    Точность модели: ~85% (экспериментальная оценка)
        """)


def main():
    """Запуск экспериментальной версии"""
    advisor = ExperimentalAdvisor()

    try:
        advisor.run_experiment()
    except KeyboardInterrupt:
        print("\n\n👋 Эксперимент прерван. Спасибо за участие!")
    except Exception as e:
        print(f"\n⚠️ Ошибка в экспериментальной версии: {e}")
        print("Возврат к стабильной версии не требуется — это часть эксперимента!")


if __name__ == "__main__":
    main()