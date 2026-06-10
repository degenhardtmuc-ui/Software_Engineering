from typing import Callable


def raise_and_handle_error(exception_type: Callable):
    print("      raise_and_handle_error(): before try")
    try:
        print("      raise_and_handle_error(): before raise")
        raise exception_type(f"Raising {exception_type.__name__}")
    except LookupError as error:
        print(f"<<< raise_and_handle_error(): caught LookupError [{error}]")
        raise
    except ValueError as error:
        print(f"<<< raise_and_handle_error(): caught ValueError [{error}]")
    print("      raise_and_handle_error(): after except")


def intermediate_fun(exception_type: Callable):
    print("   intermediate_fun(): before try")
    try:
        print("   intermediate_fun(): before calling")
        raise_and_handle_error(exception_type)
        print("   intermediate_fun(): after calling")
    except IndexError as error:
        print(f"<<< intermediate_fun(): caught IndexError [{error}]")
        raise TypeError(f"Raising inner TypeError from [{error}]") from error
    except LookupError as error:
        print(f"<<< intermediate_fun(): caught LookupError [{error}]")
        raise TypeError("Raising inner TypeError")
    except Exception as error:
        print(f"<<< intermediate_fun(): caught Exception [{error}]")
        print("   intermediate_fun(): re-raising exception")
        raise
    print("   intermediate_fun(): after except")


def outer_caller_with_try(error_type: Callable = ValueError):
    print("outer_caller(): before try")
    try:
        print("outer_caller(): before calling")
        intermediate_fun(error_type)
        print("outer_caller(): after calling")
    except Exception as error:
        print(f"<<< outer_caller(): caught Exception: {error}")
    print("outer_caller(): after except")


outer_caller_with_try(IndexError)