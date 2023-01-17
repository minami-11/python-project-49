from brain_games.games.even_odd import (start_message as even_st,
                                        question as even_q,
                                        even_odd_checker as even_answ)
from brain_games.games.calculate import (start_message as calc_st,
                                         question as calc_q,
                                         calc_checker as calc_answ)
from brain_games.games.gcd import (start_message as gcd_st,
                                   question as gcd_q,
                                   gcd_checker as gcd_answ)
from brain_games.games.progression import (start_message as progress_st,
                                           question as progress_q,
                                           progression_checker as progress_answ)
from brain_games.games.prime import (start_message as prime_st,
                                     question as prime_q,
                                     prime_checker as prime_answ)

__all__ = ['even_st', 'even_q', 'even_answ',
           'calc_st', 'calc_q', 'calc_answ',
           'gcd_st', 'gcd_q', 'gcd_answ',
           'progress_st', 'progress_q', 'progress_answ',
           'prime_st', 'prime_q', 'prime_answ'
           ]
