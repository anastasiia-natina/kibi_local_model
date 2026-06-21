from EdTechModul import SecurityEnhancedVoiceEngine 

def test_filter_blocks_garbage_input():
    filter = SecurityEnhancedVoiceEngine() # Ініціалізація фільтра
    
    # Сценарій: "Сміттєві дані" (звуки, неіснуючі команди)
    garbage_input = ["привіт", "зроби мені каву", "абракадабра", "delete system"]
    
    for input_text in garbage_input:
        # Перевіряємо, чи повертає фільтр None або False для заборонених команд
        assert filter.validate(input_text) is False, f"Фільтр пропустив небезпечну команду: {input_text}"

def test_filter_allows_valid_commands():
    filter = SecurityEnhancedVoiceEngine()
    # Список дозволених команд (Allowlist)
    valid_input = ["стрибай", "грай", "стоп"] 
    
    for input_text in valid_input:
        assert filter.validate(input_text) is True, f"Фільтр заблокував валідну команду: {input_text}"