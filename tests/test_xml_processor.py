from operator import attrgetter
from pytest import fixture

from lnreader_fb2.xml_processor import XmlProcessor


@fixture
def xml_content():
    with open("tests/files/lorem_ipsum.xml", "r") as file:
        return file.read()


def test_extract_content(xml_content):
    expected_tags = (
        'empty-line',
        'p',
        'p',
        'p',
        'p',
        'empty-line',
        'p',
    )
    expected_text = (
        None,
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod varius lectus, sit amet facilisis ipsum. Etiam viverra quam gravida rhoncus congue. Nulla hendrerit, tortor vel viverra malesuada, risus ligula convallis turpis, ut pharetra dui urna ac sapien. Donec ultricies laoreet interdum. Quisque ac placerat erat. Nunc eget ex hendrerit, pretium nibh elementum, eleifend nibh. Donec cursus a odio in volutpat. Praesent sit amet diam viverra, congue ligula in, lacinia justo.",
        'Aliquam erat volutpat. Praesent ut magna tempus, aliquet lorem ut, sodales ante. Donec et ipsum ante. Aenean eu aliquet tortor, vitae efficitur lorem. Praesent et diam vestibulum, lobortis turpis sed, facilisis enim. Integer rhoncus posuere fringilla. Quisque sed tempus urna. Nulla quam ex, dignissim in nulla in, fringilla hendrerit metus. Sed dapibus porttitor quam sed varius. Sed et tristique nisl, commodo tincidunt neque.',
        'In hac habitasse platea dictumst. Etiam augue leo, facilisis in sapien eu, cursus auctor odio. Praesent scelerisque mauris eu eros auctor, at viverra ex tincidunt. Duis tempus bibendum ligula, at rutrum odio pulvinar ut. Suspendisse euismod lorem dui, non rhoncus urna eleifend nec. Curabitur vitae faucibus justo. Sed eu laoreet augue, eu rutrum tellus. Duis aliquet eros porttitor felis volutpat blandit. Maecenas fermentum, lorem at laoreet suscipit, orci ante malesuada massa, sit amet imperdiet justo mi sed elit. Nunc lacinia, arcu eu tempor ultrices, magna enim placerat erat, eu iaculis magna lacus non sem.',
        'Etiam sed viverra magna. Quisque nec ante lorem. Phasellus eu lorem sagittis, sollicitudin eros eu, lobortis nisi. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut nibh leo, dapibus et metus at, posuere facilisis magna. Nulla vestibulum vestibulum efficitur. Nam ultricies, massa a elementum vestibulum, tellus ante faucibus enim, vitae sodales nulla ipsum sed sapien. Quisque vehicula elementum dolor vitae suscipit. Mauris at libero placerat, fermentum diam eu, faucibus ipsum. Curabitur pharetra ac lectus facilisis facilisis. Mauris malesuada pretium auctor. Integer tempus bibendum mattis. Vestibulum molestie ligula id eros aliquet luctus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam sollicitudin vehicula mauris eget tempor.',
        None,
        'Nullam sodales auctor erat. Etiam gravida, felis a cursus pellentesque, lorem neque tempus leo, quis condimentum elit diam ut mauris. In interdum ante sapien, id volutpat turpis auctor in. Phasellus eu nibh sit amet metus consectetur rutrum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin porttitor sapien eu ullamcorper tincidunt. Donec elementum, nunc sit amet suscipit ultrices, odio nunc vehicula nunc, sed tempor nibh velit id diam. Curabitur vel eleifend purus. Phasellus pulvinar mauris sem, dignissim tristique turpis laoreet quis.',
    )
    
    processor = XmlProcessor(xml_content)
    content = tuple(processor)
    
    assert tuple(map(attrgetter('tag'), content)) == expected_tags
    assert tuple(map(attrgetter('text'), content)) == expected_text
