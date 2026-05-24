# main.py
"""
Информационная система поддержки решений выбора направления обучения в университете
Автор: Студент
Версия: 1.0
"""


class StudentProfile:
    """Класс для хранения профиля студента"""

    def __init__(self):
        self.preferences = {
            "технический": 0,
            "гуманитарный": 0,
            "естественнонаучный": 0
        }
        self.finance_level = 0  # 1-5, где 5 - высокий бюджет
        self.geography_pref = ""  # "home", "regional", "any"
        self.study_features = {
            "практика": 0,
            "теория": 0,
            "исследования": 0
        }
        self.recommendations = []

    def ask_questions(self):
        """Опрос студента по ключевым вопросам"""
        print("\n" + "=" * 60)
        print("🧠 СИСТЕМА ПОДДЕРЖКИ ВЫБОРА НАПРАВЛЕНИЯ ОБУЧЕНИЯ")
        print("=" * 60)
        print("Ответьте на вопросы, чтобы получить рекомендацию.\n")

        # Блок 1: Предпочтения студента
        print("📚 БЛОК 1: Ваши предпочтения")
        print("-" * 40)
        print("Оцените интерес к следующим областям (от 1 до 5):")

        try:
            self.preferences["технический"] = int(
                input("  ▶ Интерес к техническим наукам (IT, инженерия, робототехника): "))
            self.preferences["гуманитарный"] = int(
                input("  ▶ Интерес к гуманитарным наукам (филология, история, право): "))
            self.preferences["естественнонаучный"] = int(
                input("  ▶ Интерес к естественным наукам (биология, химия, физика): "))
        except ValueError:
            print("  ⚠ Ошибка ввода! Установлены значения по умолчанию (3).")
            for k in self.preferences:
                self.preferences[k] = 3

        # Блок 2: Финансовые возможности
        print("\n💰 БЛОК 2: Финансовые возможности")
        print("-" * 40)
        print("1 - Бюджет очень ограничен (только бюджетные места)")
        print("2 - Низкий (только бесплатное обучение)")
        print("3 - Средний (готов платить до 100 тыс/год)")
        print("4 - Выше среднего (готов платить до 250 тыс/год)")
        print("5 - Высокий (без ограничений)")

        try:
            self.finance_level = int(input("  ▶ Ваш уровень финансовых возможностей (1-5): "))
            self.finance_level = max(1, min(5, self.finance_level))
        except ValueError:
            self.finance_level = 3
            print("  ⚠ Установлен средний уровень (3).")

        # Блок 3: Географические особенности
        print("\n🌍 БЛОК 3: Географические предпочтения")
        print("-" * 40)
        print("1 - Учиться только в своем городе")
        print("2 - Региональный центр (соседний город/область)")
        print("3 - Любой город России")
        print("4 - Готов учиться за границей")

        geo_choice = input("  ▶ Выберите вариант (1-4): ")
        geo_map = {"1": "home", "2": "regional", "3": "any", "4": "abroad"}
        self.geography_pref = geo_map.get(geo_choice, "any")

        # Блок 4: Особенности обучения
        print("\n🎓 БЛОК 3: Особенности обучения")
        print("-" * 40)
        print("Оцените важность для вас (1 - неважно, 5 - очень важно):")

        try:
            self.study_features["практика"] = int(input("  ▶ Наличие практики и стажировок: "))
            self.study_features["теория"] = int(input("  ▶ Фундаментальное теоретическое образование: "))
            self.study_features["исследования"] = int(input("  ▶ Возможность заниматься научной работой: "))
        except ValueError:
            for k in self.study_features:
                self.study_features[k] = 3

    def calculate_recommendations(self):
        """Расчет рекомендаций на основе ответов"""
        print("\n" + "=" * 60)
        print("📊 АНАЛИЗ ДАННЫХ И РАСЧЕТ РЕКОМЕНДАЦИЙ")
        print("=" * 60)

        # Определяем профиль на основе предпочтений
        dominant = max(self.preferences, key=self.preferences.get)

        # Список направлений с их характеристиками
        directions = [
            {
                "name": "Прикладная математика и информатика",
                "category": "технический",
                "min_finance": 2,
                "geography": ["home", "regional", "any"],
                "features": {"практика": 5, "теория": 4, "исследования": 4}
            },
            {
                "name": "Программная инженерия",
                "category": "технический",
                "min_finance": 2,
                "geography": ["regional", "any"],
                "features": {"практика": 5, "теория": 3, "исследования": 2}
            },
            {
                "name": "Лингвистика / Переводоведение",
                "category": "гуманитарный",
                "min_finance": 1,
                "geography": ["home", "regional", "any", "abroad"],
                "features": {"практика": 3, "теория": 4, "исследования": 3}
            },
            {
                "name": "Юриспруденция",
                "category": "гуманитарный",
                "min_finance": 2,
                "geography": ["home", "regional"],
                "features": {"практика": 4, "теория": 5, "исследования": 2}
            },
            {
                "name": "Биотехнология",
                "category": "естественнонаучный",
                "min_finance": 3,
                "geography": ["regional", "any"],
                "features": {"практика": 5, "теория": 4, "исследования": 5}
            },
            {
                "name": "Медицина (Лечебное дело)",
                "category": "естественнонаучный",
                "min_finance": 2,
                "geography": ["regional", "any"],
                "features": {"практика": 5, "теория": 5, "исследования": 3}
            },
            {
                "name": "Экономика и управление",
                "category": "гуманитарный",
                "min_finance": 2,
                "geography": ["home", "regional", "any"],
                "features": {"практика": 4, "теория": 3, "исследования": 2}
            },
            {
                "name": "Робототехника",
                "category": "технический",
                "min_finance": 3,
                "geography": ["regional", "any"],
                "features": {"практика": 5, "теория": 4, "исследования": 4}
            }
        ]

        # Оценка каждого направления
        scored_directions = []
        for d in directions:
            score = 0
            reasons = []

            # 1. Соответствие категории
            if d["category"] == dominant:
                score += 3
                reasons.append(f"✓ Соответствует вашим основным предпочтениям ({dominant})")
            elif self.preferences[d["category"]] >= 4:
                score += 1
                reasons.append(f"✓ У вас есть интерес к {d['category']} направлению")

            # 2. Финансовая доступность
            if self.finance_level >= d["min_finance"]:
                score += 2
                reasons.append("✓ Доступно по финансовым возможностям")
            else:
                reasons.append("✗ Может потребоваться бюджетное место")

            # 3. Географическая доступность
            if self.geography_pref in d["geography"]:
                score += 2
                reasons.append("✓ Доступно географически")

            # 4. Соответствие особенностям обучения
            feature_match = 0
            for f, val in self.study_features.items():
                if val >= d["features"][f]:
                    feature_match += 1
            if feature_match >= 2:
                score += 2
                reasons.append("✓ Соответствует вашим предпочтениям по формату обучения")

            scored_directions.append((score, d, reasons))

        # Сортировка по убыванию оценки
        scored_directions.sort(reverse=True, key=lambda x: x[0])
        self.recommendations = scored_directions[:4]  # Топ-4 рекомендации

    def show_recommendations(self):
        """Вывод рекомендаций"""
        print("\n" + "=" * 60)
        print("🎯 ВАШИ РЕКОМЕНДАЦИИ ПО НАПРАВЛЕНИЯМ ОБУЧЕНИЯ")
        print("=" * 60)

        if not self.recommendations:
            print("Не удалось сформировать рекомендации. Попробуйте пройти опрос заново.")
            return

        for i, (score, direction, reasons) in enumerate(self.recommendations, 1):
            print(f"\n🏆 #{i}: {direction['name']} (рейтинг: {score}/7)")
            print("   " + "-" * 45)
            for reason in reasons[:3]:  # Показываем основные 3 причины
                print(f"   {reason}")

            # Дополнительный совет
            if direction['min_finance'] > self.finance_level:
                print("   ⚠️ Обратите внимание: направление платное, нужен высокий балл ЕГЭ для бюджета")
            elif direction['min_finance'] <= 2:
                print("   ✅ Хорошие шансы на бюджетное место")

        print("\n" + "=" * 60)
        print("💡 СОВЕТЫ:")
        print("• Проверьте проходные баллы выбранных направлений на сайтах вузов")
        print("• Посетите дни открытых дверей в университетах")
        print("• Поговорите со студентами этих направлений")
        print("• Учитывайте свои сильные стороны при подготовке к ЕГЭ")
        print("=" * 60)

    def generate_report(self):
        """Генерация текстового отчета"""
        print("\n" + "=" * 60)
        print("📄 ИТОГОВЫЙ ОТЧЕТ ПО ПРОФИЛЮ СТУДЕНТА")
        print("=" * 60)

        print("\n📌 Профиль абитуриента:")
        dominant = max(self.preferences, key=self.preferences.get)
        print(f"  • Ведущая сфера интересов: {dominant}")
        print(f"  • Уровень финансовых возможностей: {self.finance_level}/5")
        print(f"  • Географические предпочтения: {self.geography_pref}")

        print("\n📌 Оценка предпочтений:")
        for k, v in self.preferences.items():
            bar = "█" * v + "░" * (5 - v)
            print(f"  • {k}: {bar} ({v}/5)")

        print("\n📌 Приоритеты в обучении:")
        for k, v in self.study_features.items():
            bar = "█" * v + "░" * (5 - v)
            print(f"  • {k}: {bar} ({v}/5)")


def main():
    """Главная функция программы"""
    print(""" 
    ╔══════════════════════════════════════════════════════════╗
    ║     ИНФОРМАЦИОННАЯ СИСТЕМА ПОДДЕРЖКИ РЕШЕНИЙ           ║
    ║     ВЫБОРА НАПРАВЛЕНИЯ ОБУЧЕНИЯ В УНИВЕРСИТЕТЕ         ║
    ║                                                          ║
    ║          Версия 1.0 | Учебный проект                     ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    # Создаем профиль студента
    student = StudentProfile()

    # Проводим опрос
    student.ask_questions()

    # Расчет рекомендаций
    student.calculate_recommendations()

    # Показываем рекомендации
    student.show_recommendations()

    # Генерируем отчет
    student.generate_report()

    print("\n✅ Работа программы завершена. Спасибо за использование!")


if __name__ == "__main__":
    main()