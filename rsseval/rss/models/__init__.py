import os
import importlib


def get_all_models():
    return [
        model.split(".")[0]
        for model in os.listdir("models")
        if not model.find("__") > -1 and "py" in model
    ]


names = {}
for model in get_all_models():
    mod = importlib.import_module("models." + model)
    class_name = {x.lower(): x for x in mod.__dir__()}[model.replace("_", "")]
    names[model] = getattr(mod, class_name)


def get_model(args, encoder, decoder, n_images, c_split, moco, moco_pretrained):
    if args.model == "cext":
        return names[args.model](encoder, n_images=n_images, c_split=c_split)
    elif args.model in [
        "mnistdpl",
        "mnistsl",
        "mnistltn",
        "kanddpl",
        "kandltn",
        "kandpreprocess",
        "kandclip",
        "minikanddpl",
        "mnistpcbmdpl",
        "mnistpcbmsl",
        "mnistpcbmltn",
        "mnistclip",
        "sddoiadpl",
        "sddoiacbm",
        "sddoialtn",
        "presddoiadpl",
        "boiadpl",
        "mnistcbm",
        "boiacbm",
        "boialtn",
        "kandcbm",
        "mnistnn",
        "kandnn",
        "sddoiann",
        "sddoiaclip",
        "boiann",
        "xorcbm",
        "xornn",
        "xordpl",
        "mnmathnn",
        "mnmathcbm",
        "mnmathdpl"
    ]:
        return names[args.model](
            encoder, n_images=n_images, c_split=c_split, moco=moco,
            moco_pretrained=moco_pretrained, args=args
        )  # only discriminative
    else:
        return names[args.model](
            encoder, decoder, n_images=n_images, c_split=c_split, args=args
        )
