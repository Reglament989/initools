from py_switch import Switch
import random, logging, unittest

logging.basicConfig(
    format="%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s",
    level=logging.DEBUG,
)


def test_basic():
    item = Switch(random.randrange(0, 20))
    while True:
        if item.case(random.randrange(0, 20)):
            return
        else:
            pass

    logging.info(f"Tested item [basic]: {item}")


def test_attempts():
    item = Switch(random.randrange(0, 20), attempts=random.randrange(0, 15))
    while True:
        try:
            if item.case(random.randrange(0, 20)):
                return
            else:
                pass
        except StopIteration:
            return
        except Exception as e:
            raise e

    logging.info(f"Tested item [attempts]: {item}")


def test_on_success():
    item = Switch(random.randrange(0, 20), on_success=function_on_success)
    while True:
        if item.case(random.randrange(0, 20)):
            return
        else:
            pass

    logging.info(f"Tested item [on_success]: {item}")


def test_on_fail():
    item = Switch(random.randrange(0, 20), on_fail=function_on_fail)
    while True:
        if item.case(random.randrange(0, 20)):
            return
        else:
            pass

    logging.info(f"Tested item [on_fail]: {item}")


def test_together():
    item = Switch(
        random.randrange(0, 20),
        on_success=function_on_success,
        on_fail=function_on_fail,
        attempts=random.randrange(0, 15),
    )
    while True:
        try:
            if item.case(random.randrange(0, 20)):
                return
            else:
                pass
        except StopIteration:
            return
        except Exception as e:
            raise e

    logging.info(f"Tested item [together]: {item}")


def function_on_fail():
    i = random.random()
    logging.info(f"Function on_fail complite, {i}")


def function_on_success():
    i = random.random()
    logging.info(f"Function on_success complite, {i}")
