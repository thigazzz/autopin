def add_topic_element_to_html(html: str, number_of_elements: int) -> str:
    for i in list(range(1, number_of_elements + 1)):
    
        html += f"""
        \n

        <div data-test-id="today-tab-article" class="hA- wYR zI7 iyn Hsu zmN" style="max-width:auto;width:auto">
            <div data-test-id="suggested-articles-link" class="zI7 iyn Hsu">
                <a class="Wk9 xQ4 CCY S9z eEj iyn kVc Tbt L4E e8F BG7"
                    href="any{i}" rel="" tabindex="0">
                    <div class="zI7 iyn Hsu" style="width:444px;min-height:306px">
                        <div class="ALa OVX XiG sLG urM zI7 iyn Hsu" style="padding-top:75%">
                            <div class="MIw QLY Rym ojN p6V zI7 iyn Hsu">
                                <div class="XiG zI7 iyn Hsu" style="background-color:#767676;height:100%"><img alt=""
                                        class="hCL kVc L4E MIw N7A XiG" fetchpriority="auto" loading="auto" role="presentation"
                                        src="https://i.pinimg.com/736x/83/f0/4d/83f04dedb5a7b8d397a0c1b06448706f.jpg"
                                        style="object-fit:cover" />
                                    <div class="MIw QLY Rym ojN p6V sLG zI7 iyn Hsu">
                                        <div class="Jea fBv iJk l7T zI7 iyn Hsu"
                                            style="height:100%;width:100%;background:linear-gradient(180deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.4) 100%)">
                                            <div class="jzS mQ8 un8 C9i TB_" style="width:100%">
                                                <div class="X6t zI7 iyn Hsu">
                                                    <div class="tBJ dyH iFc sAJ NAw tg7 IZT swG">any{i}</div>
                                                </div>
                                                <h2 class="lH1 dyH iFc H2s GTB NAw tg7 IZT">any{i}</h1>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
            </div>
        </div>

        \n

        """

    return html

def add_image_element_to_html(html: str, number_of_elements: int) -> str:
    for i in list(range(1, number_of_elements + 1)):
        html += """
        \n

        <div data-test-id="pin-visual-wrapper" class="XiG zI7 iyn Hsu" style="margin-top:0%;margin-bottom:0%">
            <div class="Pj7 sLG XiG ho- m1e">
                <div class="XiG zI7 iyn Hsu" style="background-color:#b07555;padding-bottom:177.54237288135593%">
                    <img alt="any" class="hCL kVc L4E MIw" fetchpriority="auto" loading="auto" src="any" />
                </div>
                <div class="KPc MIw ojN Rym p6V QLY">
                </div>
            </div>
        </div>

        \n

        """

    return html

def make_fake_html(type_of_html: str, number_of_elements: int) -> str:
    html = """
    <html>
    """
    if type_of_html == "topic":
        html = add_topic_element_to_html(html, number_of_elements)
        html += """
        \n
        </html>
        """
        return html
    else:
        html = add_image_element_to_html(html, number_of_elements)
        html += """
        \n
        </html>
        """
        return html
